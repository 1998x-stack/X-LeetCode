import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        """初始化函数，存储输入数组
        
        Args:
            nums: 整数数组
        
        """
        self.nums = nums

    def pick(self, target: int) -> int:
        """根据target随机返回其在数组中的索引
        
        使用水塘抽样算法，确保返回的索引概率相等。
        
        Args:
            target: 目标值
            
        Returns:
            target在数组中的一个随机索引
        
        """
        count = 0  # 记录target出现的次数
        chosen_index = -1  # 初始化所选索引
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1  # 遇到target，计数器加1
                # 生成一个[0, count-1]范围内的随机数，如果等于0，则更新chosen_index为当前索引
                # 这确保了每个索引被选中的概率都是1/count
                if random.randint(0, count - 1) == 0:
                    chosen_index = i
        return chosen_index

# 实例化并运行测试
# 示例数组和目标值
nums = [1, 2, 3, 3, 3]
target = 3
solution = Solution(nums)

# 运行多次pick方法来测试随机性
test_results = [solution.pick(target) for _ in range(10)]
print(test_results)