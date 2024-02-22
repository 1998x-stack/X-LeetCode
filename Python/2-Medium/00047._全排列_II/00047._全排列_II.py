from typing import List

def permuteUnique(nums: List[int]) -> List[List[int]]:
    def backtrack(start=0):
        # 如果当前排列完成，添加到结果集
        if start == len(nums):
            result.append(nums[:])
            return
        
        lookup = set()
        for i in range(start, len(nums)):
            # 跳过重复元素
            if nums[i] in lookup:
                continue
            lookup.add(nums[i])
            # 交换元素，固定当前第 start 位元素
            nums[start], nums[i] = nums[i], nums[start]
            # 递归填充下一个位置
            backtrack(start + 1)
            # 回溯，撤销操作
            nums[start], nums[i] = nums[i], nums[start]
    
    result = []
    nums.sort()  # 排序，以便去重
    backtrack()
    return result

# 测试代码
test_nums = [1, 1, 2]
print(permuteUnique(test_nums))