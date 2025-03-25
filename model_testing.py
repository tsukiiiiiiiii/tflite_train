import numpy as np
import tensorflow as tf


def load_tflite_model(model_path):
    # Load the TFLite model and allocate tensors.
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    return interpreter, input_details, output_details


def preprocess_image(image_path, input_shape):
    # Load and preprocess the image
    img = tf.io.read_file(image_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.resize(img, input_shape[:2])
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img


def predict_image(interpreter, input_details, output_details, image):
    # Set the tensor to point to the input data to be inferred
    interpreter.set_tensor(input_details[0]['index'], image)

    # Run the inference
    interpreter.invoke()

    # Get the output tensor
    output_data = interpreter.get_tensor(output_details[0]['index'])
    return output_data


def main():
    # 加载导出的 TFLite 模型
    tflite_model_path = 'export/model.tflite'  # 请根据实际路径修改
    interpreter, input_details, output_details = load_tflite_model(tflite_model_path)

    # 进行预测
    test_image_path = 'cifar100_updated/test/some_test_image.jpg'  # 替换为你的测试图像路径
    input_shape = input_details[0]['shape'][1:]
    image = preprocess_image(test_image_path, input_shape)
    predictions = predict_image(interpreter, input_details, output_details, image)

    # 打印预测结果
    predicted_class = np.argmax(predictions)
    print(f"Predicted class: {predicted_class}")


if __name__ == "__main__":
    main()
