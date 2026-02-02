def safe_calculator(func):
    def wrapper(*args, **kwargs):
        try:
            # 這裡應該要執行原始函式並回傳結果
            pass
        except (ZeroDivisionError, TypeError):
            print(f"內容錯誤")
            return 0

    return wrapper


class Product:
    def __init__(self, name, price, cost):
        self.name = name
        self.price = price
        self.__cost = cost

    @safe_calculator
    def get_profit_margin(self):
        # 公式：(售價 - 成本) / 售價
        return (self.price - self.__cost) / self.price


# 測試資料
p1 = Product("關節寶", "100", 50)  # 錯誤：price 是字串
p2 = Product("魚油", 0, 30)  # 錯誤：price 是 0

print(f"{p1.name} 毛利: {p1.get_profit_margin()}")
print(f"{p2.name} 毛利: {p2.get_profit_margin()}")
