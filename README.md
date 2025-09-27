# langchain-workflow

## 项目简介
`langchain-workflow` 是一个基于 LangChain 的大模型工作流项目，旨在简化与大语言模型的交互。该项目提供了一系列链、提示词模板和配置选项，帮助用户快速构建和执行复杂的工作流。

## 目录结构
```
langchain-workflow
├── src                     # 源代码目录
│   ├── main.py            # 应用程序入口点
│   ├── chains              # 链模块
│   │   ├── __init__.py    # 链模块初始化
│   │   ├── chat_chain.py   # 聊天链实现
│   │   └── workflow_chain.py # 工作流链实现
│   ├── prompts             # 提示词模块
│   │   ├── __init__.py    # 提示词模块初始化
│   │   └── templates.py    # 提示词模板定义
│   ├── models              # 模型模块
│   │   ├── __init__.py    # 模型模块初始化
│   │   └── llm_config.py   # 大模型配置
│   ├── utils               # 工具模块
│   │   ├── __init__.py    # 工具模块初始化
│   │   └── helpers.py      # 辅助函数
│   └── config              # 配置模块
│       ├── __init__.py    # 配置模块初始化
│       └── settings.py     # 应用程序配置
├── tests                   # 测试目录
│   ├── __init__.py        # 测试模块初始化
│   ├── test_chains.py     # 对链的单元测试
│   └── test_models.py      # 对模型的单元测试
├── data                    # 数据目录
│   └── sample_data.txt     # 示例数据
├── requirements.txt        # 项目依赖
├── .env.example            # 环境变量示例
├── .gitignore              # 版本控制忽略文件
└── README.md               # 项目文档
```

## 安装依赖
在项目根目录下运行以下命令以安装所需的依赖：
```
pip install -r requirements.txt
```

## 使用说明
1. 配置环境变量：复制 `.env.example` 文件并重命名为 `.env`，根据需要修改配置。
2. 运行应用程序：使用以下命令启动应用程序：
   ```
   python src/main.py
   ```

## 贡献
欢迎任何形式的贡献！请提交问题或拉取请求以帮助改进项目。

## 许可证
该项目遵循 MIT 许可证。