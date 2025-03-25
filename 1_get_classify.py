import tarfile
import os

# 指定压缩文件路径
file_path = r"E:\CJL\软工大二下\软件开发综合实训\tf lite\cifar-100-python.tar.gz"
# 指定解压的目标目录
extract_to_dir = r"E:\CJL\软工大二下\软件开发综合实训\tf lite\tflite-demo"

# 创建TarFile对象
with tarfile.open(file_path, 'r:gz') as tar:
    # 解压到指定目录
    tar.extractall(path=extract_to_dir)

print(f"文件已解压至: {extract_to_dir}")