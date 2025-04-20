# 使用官方Python镜像作为基础
FROM python:3.9-slim

# 设置工作目录为/app（容器内的路径）
WORKDIR /app

# 将requirements.txt复制到容器的工作目录
COPY requirements.txt .

# 安装依赖包（使用清华镜像加速）
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 将当前目录所有文件复制到容器的/app目录
COPY . .

# 暴露Flask默认端口5000
EXPOSE 5000

# 启动命令：运行app.py
CMD ["python", "app.py"]
