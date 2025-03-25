import os
import random

import tensorflow as tf
from tensorflow.keras import layers, models


# 数据集预处理，删除数据集部分图片
def dataset_partiallydelete(folder_path):
    # 设置文件夹路径
    # folder_path = 'cifar100_superclass_images/train/animals'

    # 获取所有.png图片的列表
    png_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]

    # 随机打乱列表
    random.shuffle(png_files)

    # 计算要删除的图片数量
    num_to_delete = int(len(png_files) * 0.8)

    # 获取将要删除的图片列表
    files_to_delete = png_files[:num_to_delete]

    # 删除选中的图片
    for file in files_to_delete:
        file_path = os.path.join(folder_path, file)
        os.remove(file_path)
        print(f'已删除: {file_path}')

    print(f'总计删除了 {num_to_delete} 张图片。')

dataset_partiallydelete('cifar100_updated/train/large_omnivores_and_herbivores')
'''
# 从零开始构建卷积神经网络
def load_cifar100_data(image_path):
    train_path = f"{image_path}/train"
    test_path = f"{image_path}/test"

    # 加载训练数据
    train_data = tf.keras.preprocessing.image_dataset_from_directory(
        train_path,
        label_mode='int',
        batch_size=32,
        image_size=(32, 32),
        shuffle=True
    )

    # 加载测试数据
    test_data = tf.keras.preprocessing.image_dataset_from_directory(
        test_path,
        label_mode='int',
        batch_size=32,
        image_size=(32, 32),
        shuffle=False
    )

    return train_data, test_data


def create_model():
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))

    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(100, activation='softmax'))

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model


def train_model(model, train_data, test_data, epochs=10):
    model.fit(train_data, epochs=epochs, validation_data=test_data)


image_path = 'cifar100_superclass_images'
train_data, test_data = load_cifar100_data(image_path)

model = create_model()

# 打印模型摘要
model.summary()

# 训练模型
train_model(model, train_data, test_data, epochs=10)

# 保存模型
model.save('cifar100_model.h5')
'''