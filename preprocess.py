import os
import shutil


def add_prefix_to_files(directory, prefix="acg_"):
    """为指定目录下的所有 .jpg 文件添加前缀"""
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            new_name = prefix + filename
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))


def copy_first_n_files(src_directory, dest_directory, n=2500):
    """将指定目录下的前 n 个文件复制到目标目录"""
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    files = [f for f in os.listdir(src_directory) if os.path.isfile(os.path.join(src_directory, f))]
    for i, filename in enumerate(files[:n]):
        src_file = os.path.join(src_directory, filename)
        dest_file = os.path.join(dest_directory, filename)
        if not os.path.exists(dest_file):  # 防止目标文件已存在
            shutil.copy2(src_file, dest_file)


def main():
    directory = 'acg_data'
    dest_directory = os.path.join(directory, 'acg_train2')

    # 添加类别前缀
    # add_prefix_to_files(directory)

    # 将前 1500 个文件复制到新建文件夹
    copy_first_n_files(directory, dest_directory)


if __name__ == "__main__":
    main()
