import os

import tensorflow as tf
assert tf.__version__.startswith('2')

image_path = tf.keras.utils.get_file(
      'flower_photos.tgz',
      'https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz',
      extract=True)

image_path = os.path.join(os.path.dirname(image_path), 'flower_photos')
print(image_path)


# 官网教程：https://tensorflow.google.cn/tutorials/images/classification?hl=zh_cn#%E5%9F%BA%E6%9C%AC_keras_%E6%A8%A1%E5%9E%8B