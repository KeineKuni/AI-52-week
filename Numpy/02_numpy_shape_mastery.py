import numpy as np

# 1. 建立一個包含 12 個元素的向量 (Vector)
# np.arange(12) 會生成 0 到 11 的整數
raw_data = np.arange(12)
print(f"原始一維向量: {raw_data}")
print(f"原始形狀 (shape): {raw_data.shape}\n")

# --- 學習筆記 ---
# reshape(rows, cols): 重新排列矩陣，但總元素數量必須保持不變（例如 12 = 3*4）
# -1 的妙用: 如果你不確定某個維度該是多少，可以用 -1，NumPy 會幫你自動計算
# ---

# 2. 將一維向量重塑為 3x4 的二維矩陣 (Matrix)
matrix_3x4 = raw_data.reshape(3, 4)
print("重塑後的 3x4 矩陣:")
print(matrix_3x4)

# 3. 使用 -1 自動計算維度 (例如：我想要 2 列，剩下的自動分配)
auto_matrix = raw_data.reshape(2, -1)
print(f"\n自動計算後的形狀: {auto_matrix.shape}")
print(auto_matrix)

# 4. 展平 (Flatten): 將多維矩陣變回一維向量
# 這在深度學習最後一層連接全連接層 (Dense layer) 時非常常用
flattened = auto_matrix.ravel()
print(f"\n展平後的向量: {flattened}")

# 5. 轉置 (Transpose): 行列對調
transposed = matrix_3x4.T
print("\n轉置後的矩陣 (4x3):")
print(transposed)
