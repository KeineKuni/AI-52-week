class Product:
    def __init__(self, name, price, cost) -> None:
        self.name = name
        self.price = price
        self.__cost = cost

    # def get_margin(self):
    #     margin = (self.price - self.__cost) / self.price


class Supplement(Product):
    def __init__(self, name, price, cost, is_liquid, stock):
        super().__init__(name, price, cost)
        self.is_liquid = is_liquid
        self.stock = stock


products = [
    Supplement("骨關節粉包", 126, 630, False, 5),
    Supplement("腸胃益生菌", 126, 630, False, 15),
    Supplement("寵物雞精包", 80, 299, True, 8),
]

# print("--- VitaTiere 庫存檢查報告 ---")
# for p in products:
#     if p.stock < 10:
#         msg = f"[警告] {p.name} 庫存剩餘 {p.stock}，請儘速補貨！"
#     else:
#         msg = f"[正常] {p.name} 庫存充足。"
#     print(msg)

# 一般寫法
low_stock_names = []
for p in products:
    if p.stock < 10:
        low_stock_names.append(p.name)

# 清單推導式語法 [結果 for 項目 in 清單 if 條件]
low_stock_names = [p.name for p in products if p.stock < 10]
print(low_stock_names)

discounted_prices = [p.price * 0.9 for p in products]
print(discounted_prices)
