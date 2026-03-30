import numpy as np

# 假設這是一個 3x3 的矩陣，代表 3 位客戶在 3 個類別的評分
# [食品, 用品, 寵物保健]
ratings = np.array([[5, 3, 4], [2, 4, 2], [4, 5, 5]])  # 客戶 A  # 客戶 B  # 客戶 C

# --- 學習筆記 ---
# 切片語法：array[列範圍, 行範圍]
# ':' 代表「選取全部」
# 'start:stop' 代表選取從 start 到 stop-1 的範圍
# ---

# 1. 提取「客戶 B」的所有評分 (第 1 列，索引從 0 開始)
customer_b = ratings[1, :]
print(f"客戶 B 的評分: {customer_b}")

# 2. 提取所有客戶在「寵物保健」類別的評分 (最後一行)
health_ratings = ratings[:, 2]
print(f"所有人的寵物保健評分: {health_ratings}")

# 你寫的這行會成功提取出：
# [ [5, 3],
#   [2, 4] ]
sub_matrix = ratings[:2, :2]
print("前兩位客戶在前兩個類別的評分：")
print(sub_matrix)

# --- 學習筆記 ---
# 簡寫技巧：如果從 0 開始，可以省略 0
# ratings[:2, :2] 等同於 ratings[0:2, 0:2]
# ---
