"""時間分析"""

import pandas as pd

# 1. 讀取資料
df = pd.read_csv("vitatiere_sales.csv")

# 只保留狀態為 completed 的資料
df = df[df["狀態"] == "completed"]

# 2. 清理金額欄位：移除 NT$、逗號和空格
df["淨銷售額"] = df["淨銷售額"].astype(str).str.replace("NT\$", "", regex=True)
df["淨銷售額"] = df["淨銷售額"].str.replace(",", "").str.strip()
df["淨銷售額"] = pd.to_numeric(df["淨銷售額"])

# 3. 處理時間：轉換為 Datetime 物件
df["發佈日期"] = pd.to_datetime(df["發佈日期"])

# 4. 提取月份
df["月份"] = df["發佈日期"].dt.month

monthly_revenue = df.groupby("月份")["淨銷售額"].sum()
print(monthly_revenue)

# 假設資料已經讀取並清理過金額
df["發佈日期"] = pd.to_datetime(df["發佈日期"])

# 提取下單的小時
df["下單小時"] = df["發佈日期"].dt.hour

# 看看每個小時有多少訂單
hourly_counts = df["下單小時"].value_counts().sort_index()
print(hourly_counts)


# 1. 讀取與基本清理
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

# 2. 標註週末
df["是週末"] = df["發佈日期"].dt.dayofweek >= 5

# 3. 比較營收
weekend_analysis = df.groupby("是週末")["淨銷售額"].agg(["sum", "mean", "count"])
print(weekend_analysis)

df.groupby("歸屬")["淨銷售額"].mean()
