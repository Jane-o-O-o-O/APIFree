import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 从配置文件或环境变量读取API密钥
try:
    from config import API_KEY
except ImportError:
    API_KEY = os.getenv("SILICON_FLOW_API_KEY", "your-api-key-here")

# 设置硅基流动 API 配置
os.environ["OPENAI_API_KEY"] = API_KEY

template = """
根据以下需求生成一个完整的Python项目骨架：
{requirement}

要求输出：
- 第一部分用 Markdown 格式描述完整的项目目录树
- 第二部分中显示每个文件中的函数名加上后面的注释，不要写函数实现
- 结构中要有合理的模块划分

举例：
blog_system/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── posts.py
│   │   ├── users.py

## app/main.py
## app/routers/posts.py
## app/routers/users.py

重要：请直接输出Markdown内容，不要在开头和结尾添加```markdown标记！
"""

prompt = PromptTemplate(template=template, input_variables=["requirement"])

# 使用硅基流动的 Qwen 模型
llm = ChatOpenAI(
    model="Qwen/Qwen3-Coder-480B-A35B-Instruct",
    temperature=0.7,
    base_url="https://api.siliconflow.cn/v1",
    api_key=API_KEY,
    max_tokens=4000
)

# 使用现代的 LangChain 链式调用
chain = prompt | llm | StrOutputParser()

def clean_markdown_content(content: str) -> str:
    """清理生成内容中的Markdown标记"""
    import re
    
    # 移除开头的```markdown标记
    content = re.sub(r'^```markdown\s*\n', '', content)
    content = re.sub(r'^```\s*\n', '', content)
    
    # 移除结尾的```标记
    content = re.sub(r'\n```\s*$', '', content)
    
    # 移除首尾空白行
    content = content.strip()
    
    return content

try:
    print("正在生成项目结构...")
    project_structure = chain.invoke({"requirement": "一个基于FastAPI的博客系统"})
    
    # 清理生成的内容
    project_structure = clean_markdown_content(project_structure)
    
    # 检查输出长度
    print(f"生成的内容长度: {len(project_structure)} 字符")
    
    with open("project_structure.md", "w", encoding="utf-8") as f:
        f.write(project_structure)
    
    print("项目结构已生成到 project_structure.md")
    
except Exception as e:
    print(f"错误: {e}")