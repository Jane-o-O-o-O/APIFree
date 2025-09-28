 根据你的要求，以下是一个完整的Dockerfile示例：

```Dockerfile
# 使用Python 3.11基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制并安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 配置应用启动命令
CMD ["python", "app.py"]

# 暴露合适的端口
EXPOSE 8000
```

### 解释
1. **基础镜像**: 使用 `python:3.11-slim` 作为基础镜像，这是一个轻量级的Python 3.11镜像。
2. **工作目录**: 设置工作目录为 `/app`。
3. **复制并安装依赖**: 将 `requirements.txt` 复制到镜像中，并使用 `pip` 安装依赖，使用 `--no-cache-dir` 选项优化镜像大小。
4. **复制应用代码**: 将当前目录下的所有文件复制到镜像中的 `/app` 目录。
5. **配置应用启动命令**: 使用 `CMD` 指令指定应用启动命令为 `python app.py`。
6. **暴露端口**: 使用 `EXPOSE` 指令暴露端口 8000，以便外部可以访问应用。

你可以根据你的具体应用需求调整这些步骤。