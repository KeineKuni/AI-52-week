# 1. 這是在定義「咖啡機的設計圖」
class CoffeeMachineBlueprint:
    
    # 2. 這是在設定「機器出生時」的樣子 (初始化)
    def __init__(self, given_owner_name, current_water_level):
        # self.標籤 = 傳進來的東西
        self.owner_label = given_owner_name         # 這是它取的名字（主人是誰）
        self.water_status_123 = current_water_level  # 這是它的水量狀態
        print(f"--- 嗶！{self.owner_label} 的咖啡機設定完成 ---")

    # 3. 這是在定義「它能做的動作」 (方法)
    def make_coffee_action(self, beans_type):
        # 檢查水量標籤
        if self.water_status_123 > 10:
            print(f"正在幫 {self.owner_label} 製作一杯 {beans_type} 咖啡...")
            self.water_status_123 -= 10  # 消耗水量
            print(f"製作完成！剩餘水量：{self.water_status_123}")
        else:
            print("警告：水量不足，無法動作！")

# --- 實際操作區 ---

# 4. 這一行是在「產生實體機器」，並把資料傳進去命名
# 我們傳入 "Kuni" 和 50
my_real_machine = CoffeeMachineBlueprint("Kuni", 50)

# 5. 這一行是在「叫它去做特定的動作」
# 我們叫它做 "拿鐵"
my_real_machine.make_coffee_action("拿鐵")