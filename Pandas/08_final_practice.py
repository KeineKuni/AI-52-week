import pandas as pd
import numpy as np

# 模擬一份從 WordPress 匯出的原始產品資料
raw_data = {
    "產品名稱": [
        "益生菌",
        "貓用魚油",
        "犬用魚油",
        "葉黃素",
        "化毛膏",
        "益生菌",
    ],  # 益生菌重複了
    "分類": ["腸胃保健", "皮毛保健", "皮毛保健", "眼睛保健", "腸胃保健", "腸胃保健"],
    "單價": [450, 600, 650, np.nan, 300, 450],  # 葉黃素單價缺失
    "庫存量": [20, 15, 10, 12, 5, 20],
}
df = pd.DataFrame(raw_data)

# 學習筆記：處理流程通常是「去重 -> 補值 -> 分析」
# 1. 刪除重複行
df = df.drop_duplicates()

# 2. 補齊缺失單價（假設缺漏的都填該欄位的平均值）
df["單價"] = df["單價"].fillna(df["單價"].mean())

# 3. 找出需要警示的產品：庫存量 <= 10
warning_products = df[df["庫存量"] <= 10]

# 4. 統計每個分類的平均庫存與總品項數
# 學習筆記：.agg() 可以同時套用多個函數，'count' 用來計算個數
category_summary = (
    df.groupby("分類")
    .agg({"庫存量": "mean", "產品名稱": "count"})
    .rename(columns={"庫存量": "平均庫存", "產品名稱": "產品件數"})
)

print("--- 警示產品清單 ---")
print(warning_products)

print("\n--- 分類統計摘要 ---")
print(category_summary)
