def value_check(func):
    def ex(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ZeroDivisionError, ValueError):
            print("數值有誤")
        except Exception:
            print("發生未知錯誤")
        return 0

    return ex


class Product:
    def __init__(self, name, price, cost):
        self.name = name
        self.price = price
        self.__cost = cost

    @value_check
    def get_margin(self):
        return (self.price - self.__cost) / self.price


p1, p2 = Product("骨關節", 630, 126), Product("百變怪", 0, -1)

print(p1.get_margin())
print(p2.get_margin())
