from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        寻找所有相加之和为 n 的 k 个数的组合，组合中只允许包含 1 - 9 的正整数，且每个数字仅能使用一次。

        Args:
        - k: 组合中数字的数量。
        - n: 数字的目标和。

        Returns:
        - List[List[int]]: 所有可能的组合。

        示例:
        >>> combinationSum3(3, 7)
        [[1, 2, 4]]
        >>> combinationSum3(3, 9)
        [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        """
        
        def backtrack(start: int, remaining: int, path: List[int]):
            # 如果路径长度等于 k 并且剩余和为 0，说明找到了一个有效的组合
            if len(path) == k and remaining == 0:
                result.append(path[:])  # 将当前路径的拷贝加入结果中
                return
            # 遍历从 start 到 9 的所有数字
            for i in range(start, 10):
                # 如果当前数字大于剩余和，则后面的数字也不可能满足条件，直接返回
                if i > remaining:
                    break
                # 尝试添加当前数字到路径中
                path.append(i)
                # 递归探索这个数字之后的可能性，更新剩余和
                backtrack(i + 1, remaining - i, path)
                # 回溯，移除路径中的当前数字，尝试下一个数字
                path.pop()
        
        result = []
        backtrack(1, n, [])
        return result

# 创建一个 Solution 实例
sol = Solution()

# 测试函数
test_cases = [(3, 7), (3, 9)]
for k, n in test_cases:
    print(f"k={k}, n={n}, 组合: {sol.combinationSum3(k, n)}")