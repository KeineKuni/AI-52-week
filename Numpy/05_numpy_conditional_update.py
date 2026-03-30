import numpy as np

# 1. 原始訂單數據
orders = np.array([120, 500, 2000, 150, 3000, 80, 450, 1200, 90, 600])

# 2. 設定篩選條件：金額大於 1000
cond = orders > 1000

# 3. 實戰修改：針對符合條件的訂單折抵 100 元
# --- 學習筆記 ---
# 這種寫法稱為「遮罩賦值」(Masked Assignment)。
# 它只會影響 orders 中對應為 True 的元素，其餘元素（如 120, 500）完全不動。
# ---
orders[cond] = orders[cond] - 100

print("折抵後的訂單數據：")
print(orders)

# 驗證：原本 2000 應該變成 1900，1200 應該變成 1100
