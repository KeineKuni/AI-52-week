def safe_calculator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print("❌ 錯誤：發生除以零的情況，請檢查售價是否為 0。")
            return 0
        except TypeError:
            print("❌ 錯誤：資料型別不正確，請確保輸入的是數字而非文字。")
            return 0
        except Exception as e:
            print(f"⚠️ 發生了其他未預期的錯誤: {e}")
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


p1 = Product("關節寶", 100, 50)
p2 = Product("魚油", 0, 30)

products = [p1, p2]

for p in products:
    margin = p.get_profit_margin()
    if margin > 0:
        print(f"✅ {p.name} 的毛利為：{margin:.2%}")
