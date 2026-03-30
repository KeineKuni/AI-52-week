# 範例：從 1 開始，每次跳 2 步，在 10 之前停止
print("--- 1. for 迴圈範例 ---")
for i in range(1, 10, 2):
    print(f"目前數字: {i}")
# 輸出: 1, 3, 5, 7, 9

############################################################################################

print("\n--- 2. break 與 continue 範例 ---")
numbers = [1, 2, 3, 4, 5]
target = 4

for num in numbers:
    if num == 3:
        print(f"跳過數字 {num}")
        continue  # 跳過印出 3 的步驟

    if num == target:
        print(f"已找到目標 {target}，停止搜尋！")
        break  # 找到後立即停止整個迴圈

    print(f"正在處理 {num}")
# 輸出: 正在處理 1, 正在處理 2, 跳過數字 3, 已找到目標 4，停止搜尋！


############################################################################################


def add_and_describe(a: int, b: int) -> str:
    """計算兩個數字的總和，並回傳格式化字串。"""

    # f-string: 在字串內直接嵌入變數和運算式
    sum_result = a + b
    return f"兩個數字 {a} 和 {b} 的總和是 {sum_result}"


# 呼叫函式並將結果儲存起來，再印出。
print("\n--- 3. 函式定義與回傳範例 ---")
my_result = add_and_describe(10, 5)

print(my_result)
# 輸出: 兩個數字 10 和 5 的總和是 15
