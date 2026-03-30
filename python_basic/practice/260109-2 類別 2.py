class RobotBlueprint:
    def __init__(self, itsname, itsPL):
        self.set_name = itsname
        self.set_power_level = itsPL

    def check_battery(self):
        # 請在這裡寫 print，記得要用 self 才能拿到標籤喔！
        print(f"______ 目前的電力是 ______")


# 測試用
my_bot = RobotBlueprint("Vita機器人", 99)
my_bot.check_battery()
