import pickle
import numpy as np
from matplotlib import pyplot as plt
import os

extract_to_dir = r"E:\CJL\软工大二下\软件开发综合实训\tf lite\tflite-demo\cifar-100-python"
# 假设我们处理训练集的第一个批次
batch_file = os.path.join(extract_to_dir, 'train')

# 使用pickle加载数据
with open(batch_file, 'rb') as f:
    data_dict = pickle.load(f, encoding='bytes')  # 注意：在Python 3中可能需要指定encoding

# 提取图像数据和标签
images = data_dict[b'data']

images = images.reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1)  # 转换为32x32x3的格式

# 显示第一张图像
plt.imshow(images[0])
plt.axis('off')  # 不显示坐标轴
plt.show()