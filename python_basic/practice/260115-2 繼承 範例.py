# 1. 這是「父類別」：基礎型機器人
class Robot:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} 正在移動中...")


# 2. 這是「子類別」：VitaTiere 專用銷售機器人
# 注意這裡的括號 (Robot)，代表它繼承了 Robot 的所有功能
class SalesRobot(Robot):
    def sell_product(self):
        print(f"{self.name} 正在幫 VitaTiere 推銷好吃的益生菌！")


# --- 測試區 ---
# 建立銷售機器人
nana = SalesRobot("Nana")

# 雖然 SalesRobot 裡面沒寫 move，但因為繼承了 Robot，所以它會動！
nana.move()

# 它也會自己原本就有的推銷功能
nana.sell_product()
