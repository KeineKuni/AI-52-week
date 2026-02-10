import numpy as np

sales = np.array([630, 1210, 790, 160, 888])

on_sales = sales * 0.8

# 這會回傳一個布林陣列（True/False）
mask = on_sales > 500

# 把這個 mask 丟回陣列，就能篩選出結果
expensive_items = on_sales[mask]

cheap_goods = on_sales[on_sales < 200]

revenue = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
revenue_season = revenue.reshape(4, -1)
print(revenue_season)
print(sum(revenue_season))
print(np.sum(revenue_season))
