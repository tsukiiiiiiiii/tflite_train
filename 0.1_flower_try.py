import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import pathlib
import os

dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = tf.keras.utils.get_file('flower_photos.tar', origin=dataset_url, extract=True)

image_path = os.path.join(os.path.dirname(data_dir), 'flower_photos')
print(image_path)

data_dir = pathlib.Path(data_dir).with_suffix('')

# 显示图片总数
# image_count = len(list(data_dir.glob('*/*.jpg')))
# print(image_count)

# 显示rose的第一张
# roses = list(data_dir.glob('roses/*'))
# img = PIL.Image.open(str(roses[0]))
# img.show()

# 创建数据集
# 为加载程序定义一些参数
batch_size = 32
img_height = 180
img_width = 180

train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

val_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)