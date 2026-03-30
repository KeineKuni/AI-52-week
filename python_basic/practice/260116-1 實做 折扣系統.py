"""
折扣系統
"""


class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def get_price(self):
        print(f"{self.name}是{self.price}")


class SaleProduct(Product):
    def __init__(self, name, price, reason):
        # 使用 super() 呼叫父類別的 __init__，並傳入父類別需要的參數
        super().__init__(name, price)

        # 設定子類別獨有的屬性
        self.discount_reason = reason

    def get_price(self):
        # 計算折扣價
        discount_price = int(self.price * 0.8)
        # 回傳數值，讓這行程式碼可以被賦值給變數
        return discount_price


standard_item = Product("原價", 790)
discounted_item = SaleProduct("促銷價", 790, None)

standard_item.get_price()
print(f"{discounted_item.name}是{discounted_item.get_price()}")
