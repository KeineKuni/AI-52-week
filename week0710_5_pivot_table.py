import pandas as pd

# 1. 讀取資料
df = pd.read_csv("vitatiere_sales.csv")


# 2. 定義並建立「管道分類」欄位 (這是關鍵缺失的一步！)
def classify_source(source):
    source = str(source).lower()
    if "facebook" in source or "fb" in source:
        return "Facebook"
    elif "instagram" in source or "inst" in source:
        return "Instagram"
    elif "google" in source:
        return "Google"
    else:
        return "Other"


# 執行分類
df["管道分類"] = df["歸屬"].apply(classify_source)

# 3. 建立交叉分析表
pivot_analysis = df.pivot_table(
    index="產品", columns="管道分類", values="Items sold", aggfunc="sum", fill_value=0
)

print(pivot_analysis)
