import pandas as pd

df = pd.read_csv("vitatiere_sales.csv")

df["淨銷售額"] = (
    df["淨銷售額"]
    .astype(str)
    .str.replace("NT\$", "", regex=True)
    .str.replace(",", "")
    .str.strip()
)
df["淨銷售額"] = pd.to_numeric(df["淨銷售額"])
df["發佈日期"] = pd.to_datetime(df["發佈日期"])


# 建立一個函式來分類來源
def classify_source(source):
    source = str(source).lower()  # 轉小寫方便比對
    if "facebook" in source or "fb" in source:
        return "Facebook"
    elif "instagram" in source or "l.inst" in source:
        return "Instagram"
    elif "google" in source:
        return "Google"
    elif "直接" in source:
        return "Direct"
    else:
        return "Other"


# 套用分類
df["管道分類"] = df["歸屬"].apply(classify_source)

# 一次計算總額、平均值與訂單數
analysis = df.groupby("管道分類")["淨銷售額"].agg(["sum", "mean", "count"])

# 為了閱讀方便，我們可以重新命名欄位
analysis.columns = ["總營收", "平均客單價", "訂單數"]

print(analysis)
