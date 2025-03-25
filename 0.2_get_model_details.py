import tensorflow as tf

# 加载 TFLite 模型
interpreter = tf.lite.Interpreter(model_path="export/model.tflite")
interpreter.allocate_tensors()

# 获取模型输入信息
input_details = interpreter.get_input_details()
print("Input Details:")
for i in input_details:
    print(f" - {i}")

# 获取模型输出信息
output_details = interpreter.get_output_details()
print("Output Details:")
for i in output_details:
    print(f" - {i}")

# 获取模型操作信息
ops_details = interpreter.get_tensor_details()
print("Operations Details:")
for i in ops_details:
    print(f" - {i}")

# 获取模型版本信息
version = interpreter.get_tensor_details()[0]['quantization']
print(f"TFLite Model Version: {version}")
