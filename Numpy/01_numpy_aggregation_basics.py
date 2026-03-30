import numpy as np

# 1. 建立一個模擬的感測器數據陣列 (4個感測器，每個感測器有3次讀數)
# 這裡我們用 np.random.rand 產生 0~1 之間的浮點數
data = np.array(
    [
        [0.85, 0.92, 0.88],  # 感測器 A
        [0.12, 0.15, 0.10],  # 感測器 B
        [0.45, 0.50, 0.48],  # 感測器 C
        [0.70, 0.72, 0.75],  # 感測器 D
    ]
)

print("原始數據陣列：")
print(data)

# --- 學習筆記 ---
# 在 NumPy 中，'axis' (軸) 是最重要的概念：
# axis=0: 跨行運算（垂直向下），通常得到「每一列」的統計值
# axis=1: 跨列運算（水平向右），通常得到「每一行」的統計值
# ---

# 2. 計算所有數據的總平均
total_mean = np.mean(data)
print(f"\n所有數據的總平均值: {total_mean:.4f}")

# 3. 計算每個感測器的平均值 (橫向運算，所以用 axis=1)
sensor_means = np.mean(data, axis=1)
print(f"每個感測器的平均值 (axis=1): {sensor_means}")

# 4. 找出所有數據中的最大值與最小值
max_val = np.max(data)
min_val = np.min(data)
print(f"最大值: {max_val}, 最小值: {min_val}")
