import numpy as np

sales = np.array([630, 1210, 790, 160, 888])

on_sales = sales * 0.8

# 這會回傳一個布林陣列（True/False）
mask = on_sales > 500

# 把這個 mask 丟回陣列，就能篩選出結果
expensive_items = on_sales[mask]

cheap_goods = on_sales[on_sales < 200]
