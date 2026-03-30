# 寵物產品庫存與折扣系統

inventory = [15, 8, 20]
threshold = 10

# 推薦的 Pythonic 寫法
for i, q in enumerate(inventory):  # i,q分別代表序號,值
    if q < threshold:
        print(f"產品{i+1}庫存不足,剩{q}個")

# 傳統索引寫法
for i in range(len(inventory)):
    if inventory[i] < threshold:
        print(f"產品{i+1}庫存不足,剩{inventory[i]}個")


def calculate_discount(price, discount_rate):
    return int(price * (1 - discount_rate))


print(calculate_discount(500, 0.1))
