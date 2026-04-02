import pandas as pd

# 延續之前的寵物保健產品資料
data = {
    "產品名稱": ["益生菌", "魚油", "關節保養粉", "葉黃素"],
    "單價": [450, 600, 550, 500],
    "庫存量": [20, 15, 8, 12],
    "是否缺貨": [False, False, True, False],
}
df = pd.DataFrame(data)

# --- 1. 選取特定欄位 ---
# 學習筆記：使用中括號 [] 並傳入字串，可以取得該欄位（Series）
product_names = df["產品名稱"]

# --- 2. 使用 .loc 進行標籤選取 ---
# 學習筆記：.loc[列索引, 欄位名稱]
# 選取第一列的產品名稱與單價
first_item_info = df.loc[0, ["產品名稱", "單價"]]
print(f"Line 1:\n{first_item_info}")

# --- 3. 布林過濾 (最實用！) ---
# 學習筆記：
# 步驟 A: 建立一個條件（布林序列）
# 步驟 B: 將條件放入 df[] 中，只會回傳 True 的資料
high_price_mask = df["單價"] > 500
expensive_products = df[high_price_mask]

print("\n--- 高單價產品 (>500) ---")
print(expensive_products)

# --- 4. 多重條件過濾 ---
# 學習筆記：使用 & (AND) 或 | (OR)，每個條件必須用小括號 () 包起來
# 找出單價 > 500 且 庫存量 > 10 的產品
target_products = df[(df["單價"] > 500) & (df["庫存量"] > 10)]

print("\n--- 高單價且庫存充足 ---")
print(target_products)
