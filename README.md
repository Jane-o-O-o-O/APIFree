# APIfree 智能项目生成器

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Framework](https://img.shields.io/badge/framework-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![AI Model](https://img.shields.io/badge/AI-Qwen2.5--Coder-orange.svg)](https://www.siliconflow.cn/)

## 📖 项目简介

APIfree 智能项目生成器是一个基于 AI 的自动化代码生成工具，专门用于快速构建完整的 FastAPI 项目。通过分析项目结构描述文件，自动生成包含完整业务逻辑的高质量代码，帮助开发者快速搭建生产级别的 API 项目。

### 🎯 核心特性

- **🤖 AI 驱动代码生成**: 集成硅基流动 Qwen2.5-Coder 模型，生成高质量、符合最佳实践的代码
- **📁 完整项目结构**: 自动创建标准的 FastAPI 项目架构，包含路由、模型、服务、测试等
- **🔧 智能文件分类**: 根据文件路径和内容自动识别文件类型，应用相应的代码模板
- **📝 Markdown 驱动**: 通过简单的 Markdown 文件描述项目结构即可生成完整项目
- **🎨 专业代码模版**: 内置多种文件类型的专业模板（Router、Model、Schema、Service等）
- **⚡ 批量文件生成**: 支持一次性生成整个项目的所有文件

## 🏗️ 项目架构

```
APIfree/APItest/
├── 📄 Routerchain.py          # 主要的项目生成器
├── 📄 Router.py               # 路由处理器（辅助）
├── 📄 project_structure.md    # 项目结构定义文件
├── 📄 config.py               # API配置文件
├── 📄 FIX_NOTES.md           # 修复说明文档
├── 📄 README.md              # 项目说明文档
└── 📁 __pycache__/           # Python缓存文件
```

## 🚀 快速开始

### 环境要求

- Python 3.8+
- 硅基流动 API 密钥

### 安装依赖

```bash
pip install langchain-openai
pip install python-dotenv
pip install pathlib
```

### 配置 API 密钥

1. **方法一：配置文件**
   ```python
   # config.py
   API_KEY = "your-siliconflow-api-key-here"
   ```

2. **方法二：环境变量**
   ```bash
   export SILICON_FLOW_API_KEY="your-siliconflow-api-key-here"
   ```

3. **方法三：.env 文件**
   ```bash
   # .env
   SILICON_FLOW_API_KEY=your-siliconflow-api-key-here
   ```

### 运行项目生成器

```bash
# 进入项目目录
cd APIfree/APItest

# 运行框架生成器
python Router.py

# 运行生成器
python Routerchain.py
```

## 🔄 更新日志

### v1.2.0 (2025-10-03)
- ✅ 修复了模型名称配置错误
- ✅ 改进了项目结构解析算法
- ✅ 添加了更多文件类型支持
- ✅ 优化了代码生成模板

### v1.1.0
- ✅ 添加了批量文件生成功能
- ✅ 支持自定义输出目录
- ✅ 改进了错误处理机制

### v1.0.0
- ✅ 初始版本发布
- ✅ 基础项目生成功能
- ✅ FastAPI 项目模板支持

## 🤝 贡献指南

欢迎贡献代码！请遵循以下步骤：

1. **Fork 项目**
2. **创建功能分支**: `git checkout -b feature/AmazingFeature`
3. **提交更改**: `git commit -m 'Add some AmazingFeature'`
4. **推送到分支**: `git push origin feature/AmazingFeature`
5. **开启 Pull Request**

## 📞 技术支持

- **GitHub Issues**: [提交问题](https://github.com/Jane-o-O-o-O/APIFree/issues)
- **文档**: 查看 [FIX_NOTES.md](FIX_NOTES.md) 获取详细的修复说明
- **邮箱**: support@apifree.com

## 📝 许可证

本项目基于 MIT 许可证开源。详见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

- **硅基流动**: 提供强大的 AI 模型支持
- **FastAPI**: 现代化的 Python Web 框架
- **LangChain**: 优秀的 LLM 应用开发框架
- **开源社区**: 感谢所有贡献者的支持

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给我们一个 Star！**

Made with ❤️ by [Jane-o-O-o-O](https://github.com/Jane-o-O-o-O)

</div>