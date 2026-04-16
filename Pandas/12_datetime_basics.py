import pandas as pd

# 模擬訂單資料
data = {
    "訂單日期": ["2026-01-01", "2026-01-15", "2026-02-01", "2026-02-20"],
    "金額": [1000, 1500, 1200, 2000],
}
df_sales = pd.DataFrame(data)

# --- 1. 轉換為時間型態 ---
# 學習筆記：pd.to_datetime 是工程師最常穿的「轉型鞋」，
# 沒轉成這個型態，就沒辦法提取「月份」或「年份」。
df_sales["訂單日期"] = pd.to_datetime(df_sales["訂單日期"])

# --- 2. 提取時間資訊 ---
# 學習筆記：使用 .dt 存取器，可以輕鬆抓出各種時間單位
df_sales["月份"] = df_sales["訂單日期"].dt.month
df_sales["星期幾"] = df_sales["訂單日期"].td.day_name()  # 抓出星期名稱

print("--- 帶有時間資訊的表 ---")
print(df_sales)
