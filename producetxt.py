import os

def delete_txt_files(folder_path):
    try:
        # 檢查資料夾是否存在
        if not os.path.exists(folder_path):
            print(f"資料夾 '{folder_path}' 不存在。")
            return

        # 取得資料夾中所有檔案列表
        files = os.listdir(folder_path)

        # 迭代所有檔案
        for file in files:
            # 檢查是否為 .txt 檔案
            if file.endswith(".txt"):
                file_path = os.path.join(folder_path, file)
                # 刪除檔案
                os.remove(file_path)
                print(f"刪除檔案: {file_path}")

        print("所有 .txt 檔案刪除完成。")

    except Exception as e:
        print(f"發生錯誤: {str(e)}")

# 資料夾路徑
folder_path = 'C:\\Users\\user\\OneDrive\\桌面\\人臉辨識\\'

# 呼叫函式刪除資料夾中的 .txt 檔案
delete_txt_files(folder_path)
