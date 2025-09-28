import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

class ProjectBuilder:
    def __init__(self, api_key: str, output_dir: str = "generated_project"):
        self.api_key = api_key
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # 创建LLM实例
        self.llm = ChatOpenAI(
            model="Qwen/Qwen2.5-Coder-7B-Instruct",
            temperature=0.7,
            base_url="https://api.siliconflow.cn/v1",
            api_key=api_key,
            max_tokens=3000
        )
        
        # 定义文件类型分类规则
        self.file_type_patterns = {
            "router": ["router", "api", "endpoint"],
            "model": ["model"],
            "schema": ["schema", "pydantic", "dto"],
            "service": ["service", "business", "logic"],
            "config": ["config", "setting", "env"],
            "test": ["test", "spec"],
            "migration": ["migration", "alembic", "versions"],
            "database": ["database", "db", "session"],
            "util": ["util", "helper", "common"],
            "main": ["main", "app"],
            "docker": ["dockerfile"],
            "requirements": ["requirements"]
        }
        
        # 专业化提示模板
        self.templates = {
            "router": self._get_router_template(),
            "model": self._get_model_template(),
            "schema": self._get_schema_template(), 
            "service": self._get_service_template(),
            "config": self._get_config_template(),
            "test": self._get_test_template(),
            "migration": self._get_migration_template(),
            "database": self._get_database_template(),
            "util": self._get_util_template(),
            "main": self._get_main_template(),
            "docker": self._get_docker_template(),
            "requirements": self._get_requirements_template()
        }

    def parse_project_structure(self, md_file_path: str) -> Dict[str, Dict]:
        """解析项目结构Markdown文件"""
        with open(md_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("开始解析项目结构...")
        
        # 提取目录结构 - 修复正则表达式
        tree_match = re.search(r'```\n(.*?)\n```', content, re.DOTALL)
        if not tree_match:
            # 尝试另一种格式
            tree_match = re.search(r'```[^\n]*\n(.*?)\n```', content, re.DOTALL)
        
        if not tree_match:
            raise ValueError("未找到项目目录结构")
        
        tree_content = tree_match.group(1).strip()
        print(f"提取到的目录结构:\n{tree_content}")
        
        # 解析文件描述
        file_descriptions = self._parse_file_descriptions(content)
        print(f"解析到 {len(file_descriptions)} 个文件描述")
        
        # 提取所有文件路径
        file_paths = self._extract_file_paths(tree_content)
        print(f"提取到 {len(file_paths)} 个文件路径")
        
        # 组合文件信息
        project_files = {}
        for file_path in file_paths:
            if self._should_generate_file(file_path):
                file_type = self._classify_file_type(file_path)
                project_files[file_path] = {
                    'type': file_type,
                    'description': file_descriptions.get(file_path, ''),
                    'functions': self._extract_functions(content, file_path)
                }
                print(f"添加文件: {file_path} (类型: {file_type})")
        
        return project_files

    def _should_generate_file(self, file_path: str) -> bool:
        """判断是否应该生成该文件"""
        # 跳过纯目录和某些特殊文件
        if file_path.endswith('/') or file_path in ['', 'fastapi_blog_system']:
            return False
        
        # 生成Python文件和配置文件
        generate_extensions = ['.py', '.txt', '.md', '.ini', '.mako', '']
        
        # 检查文件扩展名
        file_ext = Path(file_path).suffix
        if file_ext in generate_extensions:
            return True
            
        # 特殊文件名
        special_files = ['Dockerfile', 'README.md', 'requirements.txt', 'alembic.ini']
        if Path(file_path).name in special_files:
            return True
            
        return False

    def _parse_file_descriptions(self, content: str) -> Dict[str, str]:
        """解析文件描述"""
        descriptions = {}
        
        # 匹配文件描述部分
        pattern = r'### `([^`]+)`\s*\n(.*?)(?=###|$)'
        matches = re.findall(pattern, content, re.DOTALL)
        
        for file_path, desc in matches:
            descriptions[file_path] = desc.strip()
        
        return descriptions

    def _extract_file_paths(self, tree_content: str) -> List[str]:
        """从目录树中提取文件路径 - 修复版本"""
        files = []
        lines = tree_content.split('\n')
        path_stack = []
        
        for line in lines:
            if not line.strip():
                continue
            
            # 移除树形字符
            clean_line = re.sub(r'[├└│─\s]+', '', line)
            if not clean_line:
                continue
                
            # 计算缩进层级
            indent = 0
            for char in line:
                if char in '│ ':
                    indent += 1
                else:
                    break
            
            # 估算层级
            level = indent // 4 if indent > 0 else 0
            
            # 清理文件/目录名
            name = clean_line.rstrip('/')
            
            # 调整路径栈
            path_stack = path_stack[:level]
            
            if clean_line.endswith('/'):
                # 目录
                path_stack.append(name)
            else:
                # 文件
                if path_stack:
                    file_path = '/'.join(path_stack + [name])
                else:
                    file_path = name
                files.append(file_path)
        
        return files

    def _classify_file_type(self, file_path: str) -> str:
        """根据文件路径分类文件类型"""
        file_path_lower = file_path.lower()
        file_name = Path(file_path).name.lower()
        
        # 特殊文件处理
        if file_name == 'dockerfile':
            return "docker"
        if file_name == 'requirements.txt':
            return "requirements"
        if file_name == 'readme.md':
            return "util"
        
        # 按路径模式分类
        for file_type, patterns in self.file_type_patterns.items():
            if any(pattern in file_path_lower for pattern in patterns):
                return file_type
        
        return "util"  # 默认类型

    def _extract_functions(self, content: str, file_path: str) -> List[str]:
        """提取文件中的函数/类信息"""
        functions = []
        
        # 在文件描述中查找函数和类
        pattern = rf'### `{re.escape(file_path)}`(.*?)(?=###|$)'
        match = re.search(pattern, content, re.DOTALL)
        
        if match:
            desc_content = match.group(1)
            
            # 提取函数
            func_matches = re.findall(r'- \*\*Function\*\*: `([^`]+)`', desc_content)
            functions.extend(func_matches)
            
            # 提取类
            class_matches = re.findall(r'- \*\*Class\*\*: `([^`]+)`', desc_content)
            functions.extend(class_matches)
        
        return functions

    def generate_file_content(self, file_path: str, file_info: Dict) -> str:
        """为单个文件生成内容"""
        file_type = file_info['type']
        template = self.templates.get(file_type, self.templates['util'])
        
        # 构建提示
        prompt = PromptTemplate(
            template=template,
            input_variables=["file_path", "description", "functions"]
        )
        
        chain = prompt | self.llm | StrOutputParser()
        
        try:
            result = chain.invoke({
                "file_path": file_path,
                "description": file_info['description'],
                "functions": ', '.join(file_info['functions']) if file_info['functions'] else '无特定函数'
            })
            return result
        except Exception as e:
            print(f"生成 {file_path} 时出错: {e}")
            return self._get_fallback_content(file_path, file_type)

    def _get_fallback_content(self, file_path: str, file_type: str) -> str:
        """生成失败时的后备内容"""
        if file_path.endswith('__init__.py'):
            return '"""Package initialization file."""\n'
        elif file_type == "requirements":
            return """fastapi==0.104.1
uvicorn==0.24.0
sqlalchemy==2.0.23
pydantic==2.5.0
python-multipart==0.0.6
python-jose==3.3.0
passlib==1.7.4
alembic==1.13.0
pytest==7.4.3
httpx==0.25.2
"""
        elif file_type == "docker":
            return """FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
"""
        else:
            return f'# {file_path}\n# 自动生成失败，需要手动完成\n'

    def build_project(self, md_file_path: str):
        """构建整个项目"""
        print("开始构建项目...")
        project_files = self.parse_project_structure(md_file_path)
        
        print(f"发现 {len(project_files)} 个文件需要生成")
        
        # 按类型分组处理
        files_by_type = {}
        for file_path, file_info in project_files.items():
            file_type = file_info['type']
            if file_type not in files_by_type:
                files_by_type[file_type] = []
            files_by_type[file_type].append((file_path, file_info))
        
        # 按优先级处理
        priority_order = ['requirements', 'config', 'database', 'model', 'schema', 'service', 'router', 'main', 'test', 'migration', 'docker', 'util']
        
        for file_type in priority_order:
            if file_type in files_by_type:
                print(f"\n处理 {file_type} 类型文件...")
                for file_path, file_info in files_by_type[file_type]:
                    self._generate_and_save_file(file_path, file_info)
        
        print(f"\n项目构建完成！文件保存在: {self.output_dir}")

    def _generate_and_save_file(self, file_path: str, file_info: Dict):
        """生成并保存单个文件"""
        print(f"  生成: {file_path}")
        
        # 生成文件内容
        content = self.generate_file_content(file_path, file_info)
        
        # 创建目录结构
        full_path = self.output_dir / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 保存文件
        try:
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"    已保存: {full_path}")
        except Exception as e:
            print(f"    保存失败: {e}")

    # 添加缺失的模板
    def _get_database_template(self) -> str:
        return """
你是一个数据库连接专家。请根据以下信息生成完整的数据库连接文件：

文件路径: {file_path}
文件描述: {description}
需要实现的函数: {functions}

要求：
1. 使用SQLAlchemy创建数据库连接
2. 包含数据库会话管理
3. 添加连接池配置
4. 包含依赖注入函数
5. 添加错误处理
6. 包含完整的文档字符串

请输出完整的Python文件代码：
"""

    def _get_docker_template(self) -> str:
        return """
你是一个Docker专家。请根据以下信息生成完整的Dockerfile：

文件路径: {file_path}
文件描述: {description}

要求：
1. 使用Python 3.11基础镜像
2. 设置工作目录
3. 复制并安装依赖
4. 配置应用启动命令
5. 暴露合适的端口
6. 优化镜像大小

请输出完整的Dockerfile内容：
"""

    def _get_requirements_template(self) -> str:
        return """
你是一个Python依赖管理专家。请根据以下信息生成完整的requirements.txt：

文件路径: {file_path}
文件描述: {description}

要求：
1. 包含FastAPI和相关依赖
2. 添加数据库相关包
3. 包含测试框架
4. 添加开发工具
5. 指定具体版本号
6. 按功能分组注释

请输出完整的requirements.txt内容：
"""

    # 其他模板保持不变...
    def _get_router_template(self) -> str:
        return """
你是一个FastAPI路由专家。请根据以下信息生成完整的API路由文件：

文件路径: {file_path}
文件描述: {description}
需要实现的函数: {functions}

要求：
1. 使用FastAPI框架
2. 包含完整的路由函数实现
3. 添加适当的依赖注入和数据库会话
4. 包含请求/响应模型
5. 添加错误处理和状态码
6. 包含完整的文档字符串
7. 遵循RESTful API设计原则

请输出完整的Python文件代码：
"""

    def _get_model_template(self) -> str:
        return """
你是一个SQLAlchemy数据库模型专家。请根据以下信息生成完整的数据模型文件：

文件路径: {file_path}
文件描述: {description}
需要实现的类: {functions}

要求：
1. 使用SQLAlchemy ORM
2. 定义完整的数据模型类
3. 包含适当的字段类型和约束
4. 添加关系映射（如果需要）
5. 包含索引定义
6. 添加__repr__方法
7. 包含完整的文档字符串

请输出完整的Python文件代码：
"""

    def _get_schema_template(self) -> str:
        return """
你是一个Pydantic模式专家。请根据以下信息生成完整的数据验证模式文件：

文件路径: {file_path}
文件描述: {description}
需要实现的类: {functions}

要求：
1. 使用Pydantic BaseModel
2. 定义数据验证和序列化模式
3. 包含Create、Update、Response等变体
4. 添加字段验证器
5. 包含Config类配置
6. 添加示例数据
7. 包含完整的文档字符串

请输出完整的Python文件代码：
"""

    def _get_service_template(self) -> str:
        return """
你是一个业务逻辑服务专家。请根据以下信息生成完整的服务层文件：

文件路径: {file_path}
文件描述: {description}
需要实现的函数: {functions}

要求：
1. 实现完整的业务逻辑函数
2. 包含数据库操作
3. 添加异常处理
4. 包含数据验证
5. 添加日志记录
6. 实现事务管理
7. 包含完整的文档字符串

请输出完整的Python文件代码：
"""

    def _get_config_template(self) -> str:
        return """
你是一个配置管理专家。请根据以下信息生成完整的配置文件：

文件路径: {file_path}
文件描述: {description}
需要实现的类: {functions}

要求：
1. 使用Pydantic Settings
2. 包含环境变量读取
3. 添加配置验证
4. 包含默认值
5. 支持不同环境配置
6. 添加配置文档
7. 包含完整的文档字符串

请输出完整的Python文件代码：
"""

    def _get_test_template(self) -> str:
        return """
你是一个测试专家。请根据以下信息生成完整的测试文件：

文件路径: {file_path}
文件描述: {description}
需要实现的测试函数: {functions}

要求：
1. 使用pytest框架
2. 包含完整的单元测试
3. 添加测试装置(fixtures)
4. 包含正面和负面测试用例
5. 使用mock对象
6. 添加断言验证
7. 包含完整的文档字符串

请输出完整的Python文件代码：
"""

    def _get_migration_template(self) -> str:
        return """
你是一个数据库迁移专家。请根据以下信息生成完整的迁移文件：

文件路径: {file_path}
文件描述: {description}
需要实现的函数: {functions}

要求：
1. 使用Alembic迁移框架
2. 包含完整的迁移逻辑
3. 支持升级和降级操作
4. 添加适当的索引和约束
5. 包含数据迁移（如果需要）
6. 添加错误处理
7. 包含完整的文档字符串

请输出完整的Python文件代码：
"""

    def _get_util_template(self) -> str:
        return """
你是一个工具函数专家。请根据以下信息生成完整的工具文件：

文件路径: {file_path}
文件描述: {description}
需要实现的函数: {functions}

要求：
1. 实现实用的工具函数
2. 包含错误处理
3. 添加类型注解
4. 支持泛型（如果适用）
5. 包含单元测试
6. 添加使用示例
7. 包含完整的文档字符串

请输出完整的Python文件代码：
"""

    def _get_main_template(self) -> str:
        return """
你是一个FastAPI应用专家。请根据以下信息生成完整的主应用文件：

文件路径: {file_path}
文件描述: {description}
需要实现的函数: {functions}

要求：
1. 创建FastAPI应用实例
2. 包含路由注册
3. 添加中间件配置
4. 包含CORS设置
5. 添加异常处理器
6. 配置数据库连接
7. 包含启动和关闭事件
8. 包含完整的文档字符串

请输出完整的Python文件代码：
"""


# 使用示例
if __name__ == "__main__":
    # 配置
    API_KEY = "sk-qdsixyljzeyoessydhkwnjqnijnrylztfhccdnyoweqshyku"
    PROJECT_STRUCTURE_FILE = "project_structure.md"
    OUTPUT_DIR = "fastapi_blog_system_fixed"
    
    # 创建项目构建器
    builder = ProjectBuilder(API_KEY, OUTPUT_DIR)
    
    # 构建项目
    builder.build_project(PROJECT_STRUCTURE_FILE)