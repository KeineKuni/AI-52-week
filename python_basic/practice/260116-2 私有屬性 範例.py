class Product:
    def __init__(self, name, price):
        self.name = name
        # 加上兩個底線，變成私有屬性 🔒
        self.__price = price


standard_item = Product("原價", 790)

# 如果我現在嘗試執行這一行，你覺得會發生什麼事？
# print(standard_item.__price)
