from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

# 设置硅基流动 API 配置
os.environ["OPENAI_API_KEY"] = "sk-qdsixyljzeyoessydhkwnjqnijnrylztfhccdnyoweqshyku"

template = """
根据以下需求生成一个完整的Python项目骨架：
{requirement}

要求输出：
- 用 Markdown 格式描述完整的项目目录树
- 每个文件应包含函数名，但不要写函数实现
- 结构中要有合理的模块划分
- 包含所有必要的文件和目录
- 确保输出完整，不要遗漏任何部分
"""

prompt = PromptTemplate(template=template, input_variables=["requirement"])

# 使用硅基流动的 Qwen 模型
llm = ChatOpenAI(
    model="Qwen/Qwen2.5-Coder-7B-Instruct",
    temperature=0.7,
    base_url="https://api.siliconflow.cn/v1",
    api_key="sk-qdsixyljzeyoessydhkwnjqnijnrylztfhccdnyoweqshyku",
    max_tokens=4000  # 增加最大输出长度
)

# 使用现代的 LangChain 链式调用
chain = prompt | llm | StrOutputParser()

try:
    print("正在生成项目结构...")
    project_structure = chain.invoke({"requirement": "一个基于FastAPI的博客系统"})
    
    # 检查输出长度
    print(f"生成的内容长度: {len(project_structure)} 字符")
    
    with open("project_structure.md", "w", encoding="utf-8") as f:
        f.write(project_structure)
    
    print("项目结构已生成到 project_structure.md")
    print("前100个字符预览:")
    print(project_structure[:100])
    
except Exception as e:
    print(f"错误: {e}")