class Member:
    def __init__(self, name):
        self.name = name  # 基本設定：存名字


class VipMember(Member):
    def __init__(self, name, level):
        # 這裡不寫 self.name = name，而是叫「爸爸」來幫忙設定
        super().__init__(name)  # 把VipMember取得的name 存到Member
        self.level = level  # VIP 獨有的：等級標籤
