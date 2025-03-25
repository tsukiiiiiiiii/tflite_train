import os
from PIL import Image
import glob


def delete_jpg_files(folder_path):
    """
    删除指定文件夹中的所有 .jpg 文件

    参数:
    folder_path (str): 文件夹的路径
    """
    # 获取文件夹中所有的 .jpg 文件
    jpg_files = glob.glob(os.path.join(folder_path, '*.jpg'))

    # 遍历每个 .jpg 文件并删除
    for file_path in jpg_files:
        try:
            os.remove(file_path)
            print(f"已删除文件: {file_path}")
        except Exception as e:
            print(f"无法删除文件: {file_path}. 错误: {e}")


def convert_jpg_to_png(folder_path):
    # 检查文件夹是否存在
    if not os.path.isdir(folder_path):
        print(f"文件夹 {folder_path} 不存在。")
        return

    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)

    for file_name in files:
        # 检查文件是否为 JPG 格式
        if file_name.lower().endswith('.jpg') or file_name.lower().endswith('.jpeg'):
            # 构造完整的文件路径
            jpg_file_path = os.path.join(folder_path, file_name)
            # 打开 JPG 文件
            with Image.open(jpg_file_path) as img:
                # 构造 PNG 文件的路径
                png_file_path = os.path.join(folder_path, os.path.splitext(file_name)[0] + '.png')
                # 保存为 PNG 格式
                img.save(png_file_path, 'PNG')
                print(f"已将 {jpg_file_path} 转换为 {png_file_path}")

if __name__ == "__main__":
    # 替换为你的文件夹路径
    folder_path = "cifar100_updated/train/vehicles"
    convert_jpg_to_png(folder_path)
    delete_jpg_files(folder_path)
