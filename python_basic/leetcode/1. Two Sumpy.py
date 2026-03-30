class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in hashmap:
                # 找到了！回傳 [之前存的位置, 現在的位置]
                return [hashmap[complement], i]

            # 沒找到，把目前的數字存起來
            hashmap[n] = i
        return []  # 如果都沒找到，回傳空列表


# --- 執行部分 ---
# 1. 先實例化類別物件
sol = Solution()

# 2. 準備資料
nums = [3, 36, 8, 0, 1, -5]
target = 9

# 3. 透過物件呼叫方法
result = sol.twoSum(nums, target)
print(f"結果索引是: {result}")
