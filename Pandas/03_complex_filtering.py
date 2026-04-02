import pandas as pd

# 準備資料
data = {
    "產品名稱": ["益生菌", "魚油", "關節保養粉", "葉黃素"],
    "單價": [450, 600, 550, 500],
    "庫存量": [20, 15, 8, 12],
    "是否缺貨": [False, False, True, False],
}
df = pd.DataFrame(data)

# --- 篩選：缺貨中「或」庫存低於 10 ---
# 學習筆記：
# 1. Python 的布林值是 True / False (首字母大寫)。
# 2. | 代表「或 (OR)」，& 代表「且 (AND)」。
# 3. 每個條件務必用 () 包起來，否則運算優先權會出錯。

mask_warning = (df["是否缺貨"] == True) | (df["庫存量"] < 10)
need_restock = df[mask_warning]

print("--- 需要補貨的產品清單 ---")
print(need_restock)

# --- 進階小技巧：使用 .query() ---
# 學習筆記：當條件很多時，用字串形式寫 query 會更直覺好讀
query_result = df.query("是否缺貨 == True or 庫存量 < 10")
# print(query_result) # 結果會與上面相同
