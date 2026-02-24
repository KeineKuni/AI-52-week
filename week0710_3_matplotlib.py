import matplotlib.pyplot as plt

# 1. 準備數據（使用我們之前算好的 hourly_counts）
hourly_counts = df["發佈日期"].dt.hour.value_counts().sort_index()

# 2. 開始繪圖
plt.figure(figsize=(10, 6))  # 設定圖表大小
plt.plot(hourly_counts.index, hourly_counts.values, marker="o", color="b")

# 3. 加上標籤（因為 Matplotlib 預設不支援中文，我們先用英文標註以免亂碼）
plt.title("Sales Volume by Hour")
plt.xlabel("Hour of Day (0-23)")
plt.ylabel("Number of Orders")
plt.grid(True)

# 4. 顯示圖表
plt.show()
