# 範例
# 1. 定義「藍圖」
class RobotBlueprint:
    # 2. 初始化（出生設定）
    def __init__(self, thisisname987):
        # 把傳進來的名字，貼在「自己(self)」的標籤上
        self.my_label_xyz = thisisname987

    # 3. 定義一個「動作」
    def show_info_abc(self):
        # 從「自己(self)」身上把那個奇怪命名的標籤拿出來
        print(f"這台機器人的名字是: {self.my_label_xyz}")


# --- 使用方式 ---

# 4. 根據藍圖，製造一個真正的「物件實體」
my_robot = RobotBlueprint("小強")

# 5. 叫這個實體去做動作
my_robot.show_info_abc()
