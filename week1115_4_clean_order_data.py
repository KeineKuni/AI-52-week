import pandas as pd
import io
import re


def clean_order_data_v2(file_path):
    # --- 步驟 1: 預處理原始文字 ---
    with open(file_path, "r", encoding="utf-8-sig") as f:
        content = f.read()

    # 使用 Regex 尋找 NT$ 後面接數字與逗號的組合，並移除逗號
    # 例如把 "NT$1,200" 變成 "NT$1200"
    content = re.sub(r"(NT\$\d+),(\d+)", r"\1\2", content)

    # --- 步驟 2: 將處理過的文字轉為 DataFrame ---
    df = pd.read_csv(io.StringIO(content))

    # --- 步驟 3: 過濾與格式轉換 ---
    # 只保留已完成訂單
    df_cleaned = df[df["狀態"] == "completed"].copy()

    # 清洗金額 (現在沒有逗號了，處理更簡單)
    df_cleaned["淨銷售額"] = (
        df_cleaned["淨銷售額"]
        .astype(str)
        .str.replace("NT\$", "", regex=True)
        .str.strip()
    )
    df_cleaned["淨銷售額"] = pd.to_numeric(df_cleaned["淨銷售額"])

    # 轉換日期
    df_cleaned["發佈日期"] = pd.to_datetime(df_cleaned["發佈日期"])

    return df_cleaned


import os

# 設定你的資料存放目錄 (例如目前資料夾下的 data 資料夾)
data_folder = "./"

# 確保資料夾存在，否則先建立它
if not os.path.exists(data_folder):
    os.makedirs(data_folder)
    print(f"📁 已為你建立 {data_folder} 資料夾，請把 CSV 丟進去再執行一次！")

# 1. 取得資料夾內所有檔案
files = os.listdir(data_folder)

print(f"🔍 掃描中... 發現 {len(files)} 個檔案")

# 2. 開始遍歷並處理
for file_name in files:
    # 只處理 .csv 檔案
    if file_name.endswith(".csv"):
        full_path = os.path.join(data_folder, file_name)

        # 呼叫我們先前強大的清洗函式
        try:
            df = clean_order_data_v2(full_path)

            # 計算該月份摘要
            total_revenue = df["淨銷售額"].sum()
            count = len(df)

            print(f"✅ 檔案：{file_name}")
            print(f"   📊 成功訂單：{count} 筆 | 💰 營收：NT$ {total_revenue:,.0f}")
        except Exception as e:
            print(f"❌ 處理 {file_name} 時發生錯誤：{e}")

print("\n✨ 所有報表掃描完成！")
