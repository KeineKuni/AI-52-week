import numpy as np

orders = np.array([120, 500, 2000, 150, 3000, 80, 450, 1200, 90, 600])
cond = orders > 1000
big_orders = orders[cond]
print(big_orders)
