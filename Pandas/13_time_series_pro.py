import pandas as pd

# 模擬一個月的訂單資料
data = {
    "訂單日期": pd.date_range(
        start="2026-03-01", periods=10, freq="D"
    ),  # 學習筆記：快速生成連續日期
    "金額": [1200, 800, 1500, 2200, 1800, 900, 1100, 1300, 2500, 1600],
}
df = pd.DataFrame(data)

# --- 1. 提取更多時間維度 ---
# 學習筆記：.dt.weekday 會回傳 0-6 (週一到週日)
df["月份"] = df["訂單日期"].dt.month
df["星期"] = df["訂單日期"].dt.day_name()
df["是否為週末"] = df["訂單日期"].dt.weekday >= 5

# --- 2. 分析週末與平日的平均業績 ---
weekend_analysis = df.groupby("是否為週末")["金額"].mean().reset_index()

print("--- 週末與平日業績對比 ---")
print(weekend_analysis)
