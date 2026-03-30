# 1. 定義類別：後面沒有括號，也沒有變數
class VitaProduct:
    def __init__(self, title_abc, price_123):
        self.name = title_abc
        self.price = price_123


# 2. 使用類別：後面有括號，並傳入變數
p1 = VitaProduct("益生菌", 500)
