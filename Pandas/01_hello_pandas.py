import pandas as pd

# 學習筆記：
# 1. pd 是 pandas 的慣用縮寫。
# 2. DataFrame 就像是一個由多個 Series 組成的字典。
# 3. 每一把「Key」會變成欄位名稱 (Columns)，「Value」列表則是資料。

# 模擬一些寵物保健產品的數據
data = {
    "產品名稱": ["益生菌", "魚油", "關節保養粉", "葉黃素"],
    "單價": [450, 600, 550, 500],
    "庫存量": [20, 15, 8, 12],
    "是否缺貨": [False, False, True, False],
}

# 建立 DataFrame
df = pd.DataFrame(data)

# 顯示前幾行資料 (預設顯示 5 行)
print("--- 產品清單 ---")
print(df.head())

# 學習筆記：
# 使用 df.info() 可以快速查看資料型態與是否有缺失值 (NaN)
print("\n--- 資料摘要 ---")
df.info()
