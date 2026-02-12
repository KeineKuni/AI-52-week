import pandas as pd

# 讀取 CSV 檔案
df = pd.read_csv("vitatiere_sales.csv")

# 顯示前 5 筆資料，看看長什麼樣子
print(df.head())

# 顯示欄位名稱、非空值數量以及資料型態 (Data Type)
df.info()
