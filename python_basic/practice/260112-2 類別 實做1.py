class VitaBot:
    def __init__(self, bot_name):
        self.nickname = bot_name

    def say_hi(self):
        # 這裡該怎麼寫，才能讓機器人說出：「你好，我是 [它的名字]」？
        print(f"你好，我是 {self.nickname}")

# 呼叫
my_bot = VitaBot("可思")
my_bot.say_hi()