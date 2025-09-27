from langchain.prompts import PromptTemplate

class ThreeLayerPromptTemplates:
    """三层工作流的提示词模板集合"""
    
    # 第一层：需求分析模板
    REQUIREMENT_ANALYSIS_TEMPLATE = """
用户需求: {user_requirement}
你是一名经验丰富的软件系统分析师，具备将自然语言需求转化为清晰可执行的编程任务描述的能力。
当用户输入自然语言时，你需要完成以下工作：

1.需求抽象
1.1提取用户的核心目标与场景。
1.2判断系统需要实现的功能。

2.输入与输出规范
2.1明确系统的预期输入（数据来源、参数类型、格式等）。
2.2明确系统的预期输出（返回结果、处理形式、表现方式等）。

3.功能点拆解
3.1列出系统的主要功能模块。
3.2标注每个模块的关键逻辑。
3.3如果可能，给出依赖或扩展点。

4.交付格式
以结构化说明文档的形式输出，分为以下部分：
需求描述,输入规范,输出规范,功能点说明

注意事项/边界条件

风格要求

使用简洁清晰、工程师可直接实现的语言。

不写具体代码，只输出分析后的任务说明。
现在请根据以下用户需求生成结构化的任务描述：
"""

    # 第二层：架构设计模板
    ARCHITECTURE_DESIGN_TEMPLATE = """
需求分析结果: {requirement_analysis}
你是一名资深的 Python 系统架构师。你的任务是根据解析层输出的任务描述，生成对应的Python模块和代码结构，包括文件路径、模块/类和函数接口设计。

请严格按以下要求输出，使用 Markdown 格式，遵循 PEP8 命名规范：

# 项目结构（Project Structure）

## 目录结构
用树形结构列出目录、包与文件（包含必要的 `__init__.py`）。

## 模块说明
为每个文件简要标注职责，列出关键的类与函数签名（仅声明，不展开实现）。

## 测试结构
包含 `tests/` 测试目录的占位与关键用例文件。

## 配置文件
如有配置与工具模块（如 `config/`, `utils/`），一并标注。

## 示例输出格式：
```
project_name/
├── src/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py          # 用户数据模型
│   ├── services/
│   │   ├── __init__.py
│   │   └── auth_service.py  # 认证服务逻辑
│   └── main.py              # 应用入口
├── tests/
│   ├── __init__.py
│   ├── test_models.py       # 模型测试
│   └── test_services.py     # 服务测试
├── config/
│   └── settings.py          # 配置文件
└── requirements.txt         # 依赖文件
```

**模块详细说明：**
- `src/models/user.py`: 
  - `class User`: 用户数据模型
  - `def validate_email(email: str) -> bool`: 邮箱验证
- `src/services/auth_service.py`:
  - `class AuthService`: 认证服务类
  - `def register_user(username: str, password: str, email: str) -> dict`: 用户注册
  - `def login_user(username: str, password: str) -> dict`: 用户登录

现在请根据以下任务描述生成上述结构：
"""

    # 第三层：代码实现模板
    CODE_IMPLEMENTATION_TEMPLATE = """
根据架构设计实现完整代码：{architecture_design}
作为Python开发工程师，请严格按照上述架构设计实现完整代码。

要求:
1. **严格遵循架构设计中的文件结构和函数名**
2. **每个文件都要实现，不能遗漏**
3. **函数必须有完整的实现，不能只有pass**
4. **导入路径要正确**
5. **代码要能实际运行**

输出格式:
```python
# filepath: 文件路径
# 文件完整代码
```

请逐个文件实现，确保：
- 按照架构设计中的目录结构
- 实现架构设计中列出的所有类和函数
- 代码逻辑完整可运行
- 不要添加架构设计中没有的额外文件

开始实现：
"""

    @staticmethod
    def get_requirement_analysis_prompt():
        """获取需求分析提示词模板"""
        return PromptTemplate(
            input_variables=["user_requirement"],
            template=ThreeLayerPromptTemplates.REQUIREMENT_ANALYSIS_TEMPLATE
        )
    
    @staticmethod
    def get_architecture_design_prompt():
        """获取架构设计提示词模板"""
        return PromptTemplate(
            input_variables=["requirement_analysis"],
            template=ThreeLayerPromptTemplates.ARCHITECTURE_DESIGN_TEMPLATE
        )
    
    @staticmethod
    def get_code_implementation_prompt():
        """获取代码实现提示词模板"""
        return PromptTemplate(
            input_variables=["architecture_design"],
            template=ThreeLayerPromptTemplates.CODE_IMPLEMENTATION_TEMPLATE
        )

# 便捷访问函数
def get_template(template_type: str):
    """根据类型获取对应的模板"""
    templates = {
        "requirement": ThreeLayerPromptTemplates.get_requirement_analysis_prompt(),
        "architecture": ThreeLayerPromptTemplates.get_architecture_design_prompt(),
        "implementation": ThreeLayerPromptTemplates.get_code_implementation_prompt()
    }
    return templates.get(template_type)