import pandas as pd

# 模擬資料：魚油出現兩次，但價格被輸入錯了
data = {
    "產品名稱": ["益生菌", "魚油", "魚油", "葉黃素"],
    "單價": [450, 600, 700, 500],
    "庫存量": [20, 15, 12, 10],
}
df = pd.DataFrame(data)

# --- 1. 預設刪除 (整列需完全相同) ---
# 因為 600 != 700，這兩行都會被保留
default_drop = df.drop_duplicates()

# --- 2. 根據特定欄位刪除 ---
# 學習筆記：
# subset: 指定判斷重複的欄位
# keep: 'first' (保留第一筆, 預設), 'last' (保留最後一筆), False (全部刪除)
clean_by_name = df.drop_duplicates(subset=["產品名稱"], keep="first")

print("--- 根據產品名稱去重 (保留第一筆) ---")
print(clean_by_name)
