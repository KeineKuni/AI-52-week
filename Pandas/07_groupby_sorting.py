import pandas as pd

# 準備 VitaTiere 產品資料
data = {
    "產品名稱": ["益生菌", "貓用魚油", "犬用魚油", "葉黃素", "化毛膏"],
    "分類": ["腸胃保健", "皮毛保健", "皮毛保健", "眼睛保健", "腸胃保健"],
    "單價": [450, 600, 650, 500, 300],
    "庫存量": [20, 15, 10, 12, 30],
}
df = pd.DataFrame(data)

# --- 計算每個分類的平均單價並排序 ---
# 學習筆記：
# 1. mean() 會計算平均值。
# 2. sort_values() 預設是升冪排列 (從小到大)。
# 3. ascending=False 則是降冪排列 (從大到小)。

avg_price_by_category = df.groupby("分類")["單價"].mean().sort_values(ascending=False)

print("--- 各分類平均單價（高到低） ---")
print(avg_price_by_category)

# 學習筆記：
# 如果你想讓結果看起來像一個乾淨的表格，可以使用 .reset_index()
# 這會把原本變成「索引」的分類，變回正常的「欄位」。
clean_table = avg_price_by_category.reset_index()
print("\n--- 格式化後的結果 ---")
print(clean_table)
