import os
from PIL import Image
import base64
import xml.etree.ElementTree as ET

def png_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        # 读取 PNG 图像文件并将其转换为 Base64 编码字符串
        base64_encoded = base64.b64encode(image_file.read()).decode('utf-8')
    return base64_encoded

def create_xml_with_base64(base64_data, xml_filename):
    # 创建 XML 文档
    root = ET.Element("root")
    data_element = ET.SubElement(root, "ImageData")
    data_element.text = base64_data

    # 将 XML 写入文件
    tree = ET.ElementTree(root)
    tree.write(xml_filename)

def process_folder(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        relative_path = os.path.relpath(root, input_folder)
        output_folder_path = os.path.join(output_folder, relative_path)

        # 创建输出文件夹
        os.makedirs(output_folder_path, exist_ok=True)

        for file in files:
            if file.lower().endswith('.png'):
                png_image_path = os.path.join(root, file)

                # 将 PNG 图像转换为 Base64 编码字符串
                base64_data = png_to_base64(png_image_path)

                # 创建 XML 文件的名称，保持相对路径
                xml_filename = os.path.join(output_folder_path, os.path.splitext(file)[0] + ".xml")

                # 创建 XML 文档，并将 Base64 数据添加到 XML 中
                create_xml_with_base64(base64_data, xml_filename)

if __name__ == "__main__":
    # 指定原始图像文件夹和输出 XML 文件夹
    input_folder = "C:\\Users\\user\\Downloads\\iam_words\\words"
    output_folder = "C:\\Users\\user\\Downloads\\iam_words\\xml"

    # 处理每个原始文件夹
    for folder_name in os.listdir(input_folder):
        folder_path = os.path.join(input_folder, folder_name)
        if os.path.isdir(folder_path):
            process_folder(folder_path, output_folder)
