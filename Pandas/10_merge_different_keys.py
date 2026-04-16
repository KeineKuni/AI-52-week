import pandas as pd

# 表 A：產品基本資訊 (使用 '產品ID')
df_products = pd.DataFrame(
    {"產品ID": [101, 102, 103], "產品名稱": ["益生菌", "魚油", "葉黃素"]}
)

# 表 B：銷售紀錄 (使用 'PID')
df_sales = pd.DataFrame({"PID": [101, 101, 102, 105], "銷售數量": [2, 5, 1, 3]})

# --- 使用 left_on 與 right_on 合併 ---
# 學習筆記：
# 1. left_on: 左表要對照的欄位
# 2. right_on: 右表要對照的欄位
# 3. 合併後會同時保留 '產品ID' 和 'PID'，通常我們會再刪除其中一個。

merged_inner = pd.merge(
    df_products, df_sales, left_on="產品ID", right_on="PID", how="inner"
)

# 學習筆記：使用 .drop(columns='PID') 來移除重複的欄位
final_df = merged_inner.drop(columns="PID")

print("--- 銷售紀錄與產品資訊對照 (Inner) ---")
print(final_df)
