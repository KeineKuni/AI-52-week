class PatrolRobot:

    def __init__(self, bot_id, battery_level):
        self.bot_id = bot_id
        self.battery_level = battery_level

    def move(self, distance):
        # 1. 消耗電力（移動 1 公尺消耗 2% 電力）
        energy_cost = distance * 2

        self.battery_level -= energy_cost

        print(f"機器人 {self.bot_id} 移動了 {distance} 公尺。")
        print(f"剩餘電力：{self.battery_level}%")


# --- 實作區 ---
# 建立一台編號為 "V-01"，電力 100% 的機器人
my_bot = PatrolRobot("V-01", 100)

# 叫它移動 10 公尺
my_bot.move(10)
