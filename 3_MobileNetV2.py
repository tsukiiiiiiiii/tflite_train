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

image_path = 'cifar100_updated/train'

data = DataLoader.from_folder(image_path)
train_data, test_data = data.split(0.9)

model = image_classifier.create(train_data, epochs=6)

loss, accuracy = model.evaluate(test_data)

model.export(export_dir='export')

print("complete")
print(f"Loss: {loss}, Accuracy: {accuracy}")
