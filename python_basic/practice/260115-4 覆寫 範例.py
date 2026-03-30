class Robot:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} 慢吞吞地走...")


class RacingRobot(Robot):
    # 這裡我們「覆寫」了父類別的方法
    # 只要名字一模一樣，子類別的動作就會取代父類別
    def move(self):
        print(f"{self.name} 以時速 200 公里狂飆！🏎️")


# 測試
normal_bot = Robot("普通號")
fast_bot = RacingRobot("閃電號")

normal_bot.move()  # 輸出：慢吞吞地走...
fast_bot.move()  # 輸出：以時速 200 公里狂飆！
