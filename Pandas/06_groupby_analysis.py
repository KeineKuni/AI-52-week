import pandas as pd

data = {
    "產品名稱": ["益生菌", "貓用魚油", "犬用魚油", "葉黃素", "化毛膏"],
    "分類": ["腸胃保健", "皮毛保健", "皮毛保健", "眼睛保健", "腸胃保健"],
    "單價": [450, 600, 650, 500, 300],
    "庫存量": [20, 15, 10, 12, 30],
}
df = pd.DataFrame(data)

# --- 使用 Groupby 進行分類統計 ---
# 學習筆記：
# 1. groupby('分類'): 先依照分類把資料「分堆」。
# 2. ['庫存量']: 指定我們要計算的數字欄位。
# 3. .sum(): 指定計算方式 (加總)。
inventory_sum = df.groupby("分類")["庫存量"].sum()

print("--- 各分類總庫存 ---")
print(inventory_sum)

# 學習筆記：也可以一次計算多個統計指標 (.agg)
summary = df.groupby("分類")["單價"].agg(["mean", "max", "count"])
print("\n--- 各分類單價摘要 (平均/最高/件數) ---")
print(summary)
