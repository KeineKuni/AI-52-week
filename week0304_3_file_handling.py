class Product:
    def __init__(self, name, price, cost):
        self.name = name
        self.price = price
        self._cost = cost


class Supplement(Product):
    def __init__(self, name, price, cost, stock=0):
        super().__init__(name, price, cost)
        self.stock = stock

    def get_margin(self):
        if self.price == 0:
            return 0
        return (self.price - self._cost) / self.price


all_products = []

try:
    with open("products.txt", "r", encoding="utf-8") as file:
        for line in file:
            data = line.strip().split(",")
            if len(data) == 3:
                name = data[0]
                price = float(data[1])
                cost = float(data[2])

                new_product = Supplement(name, price, cost, 0)
                all_products.append(new_product)
except FileNotFoundError:
    print("找不到 products.txt 檔案，請確認檔案路徑。")

# 輸出成果到螢幕與檔案
with open("report.txt", "w", encoding="utf-8") as file:
    file.write("VitaTiere 毛利報告\n")
    file.write("------------------\n")

    for p in all_products:
        margin = p.get_margin()
        # 這裡會成功，因為 p 現在是 Supplement 物件了
        print(f"成功載入：{p.name}，售價：{p.price}")

        if margin > 0:
            file.write(f"產品：{p.name} | 毛利：{margin:.2%}\n")

print("\n✅ 報告已生成至 report.txt")
