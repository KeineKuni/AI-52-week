import pandas as pd

# 表 A：產品基本資訊
df_products = pd.DataFrame(
    {"產品ID": [101, 102, 103, 104], "產品名稱": ["益生菌", "魚油", "葉黃素", "化毛膏"]}
)

# 表 B：倉庫庫存位置
df_warehouse = pd.DataFrame(
    {
        "產品ID": [101, 102, 103, 105],  # 注意：這裡有 105，但沒有 104
        "儲位編號": ["A-01", "A-02", "B-05", "C-03"],
    }
)

# --- 使用 Left Join 合併 ---
# 學習筆記：
# 1. left: 左邊的 DataFrame
# 2. right: 右邊的 DataFrame
# 3. on: 用來對照的欄位名稱 (Key)
# 4. how: 合併方式 ('left', 'right', 'inner', 'outer')

merged_df = pd.merge(df_products, df_warehouse, on="產品ID", how="left")

# 學習筆記：
# 因為使用了 left join，產品ID 104 (化毛膏) 會被保留，
# 但因為它在倉庫表中沒有資料，所以「儲位編號」會顯示為 NaN。

print("--- 合併後的產品位置表 ---")
print(merged_df)
