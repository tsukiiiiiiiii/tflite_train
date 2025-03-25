import os
import pickle
import numpy as np
from PIL import Image

# 设置数据集的路径和保存图片的路径
dataset_path = './cifar-100-python'
save_path = './cifar100_superclass_images'

# 确保保存路径存在
os.makedirs(save_path, exist_ok=True)


# 加载 CIFAR-100 数据集
def load_cifar100(file):
    with open(file, 'rb') as fo:
        data = pickle.load(fo, encoding='bytes')
    return data


# 获取数据和标签
train_data = load_cifar100(os.path.join(dataset_path, 'train'))
test_data = load_cifar100(os.path.join(dataset_path, 'test'))
meta_data = load_cifar100(os.path.join(dataset_path, 'meta'))

# 获取类别名称和超类名称
label_names = [label.decode('utf-8') for label in meta_data[b'fine_label_names']]
superclass_names = [label.decode('utf-8') for label in meta_data[b'coarse_label_names']]


def save_images(data, dataset_type):
    images = data[b'data']
    fine_labels = data[b'fine_labels']
    coarse_labels = data[b'coarse_labels']
    filenames = data[b'filenames']

    for idx, (image, fine_label, coarse_label, filename) in enumerate(
            zip(images, fine_labels, coarse_labels, filenames)):
        # 获取超类名
        superclass_name = superclass_names[coarse_label]
        # 创建超类文件夹
        superclass_folder = os.path.join(save_path, dataset_type, superclass_name)
        os.makedirs(superclass_folder, exist_ok=True)
        # 重塑图像并保存为 PNG 格式
        image = image.reshape(3, 32, 32).transpose(1, 2, 0)
        image_pil = Image.fromarray(image)
        image_path = os.path.join(superclass_folder, f'{filename.decode("utf-8")}.png')
        image_pil.save(image_path)


# 保存训练集图片
save_images(train_data, 'train')
# 保存测试集图片
save_images(test_data, 'test')

print("CIFAR-100 数据集已成功保存为多层文件夹结构（按超类），格式为 PNG 图片。")