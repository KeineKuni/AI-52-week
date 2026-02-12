import numpy as np

# 每一列代表一個產品，每一行代表一天的銷量
# (5個產品, 3天)
sales_matrix = np.array(
    [
        [10, 12, 15],  # 產品 A
        [20, 18, 22],  # 產品 B
        [5, 7, 6],  # 產品 C
        [30, 35, 40],  # 產品 D
        [12, 10, 11],  # 產品 E
    ]
)

print(np.sum(sales_matrix[4 - 1, :]))
print(np.sum(sales_matrix[:, 2]))
