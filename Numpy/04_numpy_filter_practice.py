import numpy as np

# 1. 訂單數據
orders = np.array([120, 500, 2000, 150, 3000, 80, 450, 1200, 90, 600])

# 2. 建立判斷條件 (這會產生一個布林陣列)
# --- 學習筆記 ---
# 這行代碼背後的操作是：[120>1000, 500>1000, 2000>1000, ...]
# 結果會是 [False, False, True, False, True, ...]
# ---
cond = orders > 1000

# 3. 使用遮罩提取資料
# --- 學習筆記 ---
# orders[cond] 只會取出 cond 中對應位置為 True 的元素
# ---
big_orders = orders[cond]

print(f"大額訂單金額：{big_orders}")
