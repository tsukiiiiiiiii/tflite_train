import os
import numpy as np
import tensorflow as tf

assert tf.__version__.startswith('2')

from tflite_model_maker import model_spec
from tflite_model_maker import image_classifier
from tflite_model_maker.config import ExportFormat
from tflite_model_maker.config import QuantizationConfig
from tflite_model_maker.image_classifier import DataLoader

import matplotlib.pyplot as plt

# 加载数据
image_path = 'cifar100_updated/train'
data = DataLoader.from_folder(image_path)
train_data, test_data = data.split(0.9)

# 使用EfficientNet Lite0模型规格
spec = model_spec.get('efficientnet_lite0')

# 创建模型
model = image_classifier.create(train_data, model_spec=spec, epochs=2)

# 打印模型的类型和结构
model.summary()

# 评估模型
loss, accuracy = model.evaluate(test_data)

# 导出模型
model.export(export_dir='export')

print("complete")
print(f"Loss: {loss}, Accuracy: {accuracy}")
