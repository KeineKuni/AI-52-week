class Product:
    def __init__(self, name, price, cost):
        self.name = name
        self.price = price
        self.__cost = cost


# 這是我們從資料庫抓下來的原始資料
raw_data = [
    {"name": "魚油", "price": 200, "cost": 120},
    {"name": "關節寶", "price": 100, "cost": 50},
    {"name": "錯誤測試", "price": 0, "cost": 30},
]
# 我們可以結合之前的 Product 類別與迴圈
all_product_objects = []

for item in raw_data:
    # 建立物件並存入新清單
    all_product_objects.append(Product(item["name"], item["price"], item["cost"]))
