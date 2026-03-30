class SuperRobot:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def upgrade_level(self):
        self.level += 1


robot_nana = SuperRobot("Nana", 6)
robot_nana.upgrade_level()

print(f"我是機器人{robot_nana.name},我現在等級是{robot_nana.level}")
