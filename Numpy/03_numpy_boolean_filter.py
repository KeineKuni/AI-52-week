import numpy as np

# 1. 假設這是一組溫度感測器的讀數
temperatures = np.array([25.4, 26.1, 999.0, 25.8, -50.0, 26.5])

print(f"原始數據: {temperatures}")

# --- 學習筆記 ---
# 布林篩選的原理：
# 1. 先產生一個「布林遮罩 (Mask)」，這是一個全是 True/False 的陣列。
# 2. 將遮罩放進中括號 []，NumPy 只會保留 True 的部分。
# ---

# 2. 定義正常的溫度範圍 (20 到 40 度之間)
# 建立遮罩：找出大於 20 且 小於 40 的數值
mask = (temperatures > 20) & (temperatures < 40)

print(f"布林遮罩 (哪些符合條件?): {mask}")

# 3. 提取正常數據
normal_temps = temperatures[mask]
print(f"篩選後的正常數據: {normal_temps}")

# 4. 進階：直接將異常值「修正」為平均值
# 這裡我們把不是正常範圍內的數值，全部設定為 25.0
temperatures[~mask] = 25.0  # '~' 代表「非」，即不符合條件的部分
print(f"修正異常值後的數據: {temperatures}")
