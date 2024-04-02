import csv
import os

# 讀取CSV檔案
csv_file = './list_bbox_celeba.csv'

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # 跳過標頭行

    # 逐行處理CSV內容
    for i,row in enumerate(reader):
        # 提取id和數據
        img_id, x, y, w, h = row
        img_id = os.path.splitext(img_id)[0]  # 去除文件擴展名
       
        # 構建txt檔案名稱和內容
        txt_filename = f"{img_id}.txt"
        txt_content = f"{i+1} {x} {y} {w} {h}"  # 將id包含在內容中

        # 寫入到txt檔案
        with open(txt_filename, 'w') as txt_file:
            txt_file.write(txt_content)
