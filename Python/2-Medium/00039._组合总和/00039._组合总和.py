from typing import List
"""
- **排序**：通过对 `candidates` 进行排序，我们既优化了搜索效率（使得可以更早地剪枝），也避免了生成重复的组合。
- **深度优先搜索（DFS）与回溯**：我们使用了DFS来遍历所有可能的组合。通过添加元素到当前路径中，如果路径的总和等于目标值，则将其添加到结果列表中。如果当前路径的总和超过目标值或者所有可能的路径都已探索，我们回溯到上一步，即撤销最后一个选择，以探索其他可能的路径。
- **剪枝**：在每次递归调用前，我们检查加上当前候选数字后是否会超过目标和。如果会，就跳过当前数字及之后的所有数字，因为数组已排序，之后的数字只会更大。
- **递归**：通过递归调用 `dfs` 函数，允许我们重复选择相同的数字（通过不增加 `start` 的值），同时也探索了所有不同的选择路径。
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        寻找所有组合的总和等于目标值的组合。
        
        Args:
        candidates: 一个无重复元素的列表。
        target: 目标和。
        
        Returns:
        一个列表，包含所有可能的组合，每个组合的和等于目标值。
        
        """
        # 对候选数组进行排序，有助于剪枝
        candidates.sort()
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates: List[int], target: int, start: int, path: List[int], res: List[List[int]]):
        """
        深度优先搜索函数，用于找到所有符合条件的组合。
        
        Args:
        candidates: 候选数字列表。
        target: 目标和。
        start: 当前考虑的候选数字的起始位置。
        path: 当前路径（已选择的候选数字的组合）。
        res: 结果列表，存储所有符合条件的组合。
        """
        # 基本情况：如果当前总和等于目标值，则将路径添加到结果中
        if target == 0:
            res.append(path.copy())
            return
        for i in range(start, len(candidates)):
            # 剪枝：如果当
            # 前数字加上路径中的数字总和超过目标值，则跳过
            if target < candidates[i]:
                break
            # 选择当前数字，加入路径
            path.append(candidates[i])
            # 递归调用，注意新的目标值减去当前数字，和起始位置为当前位置（允许重复选择）
            self.dfs(candidates, target - candidates[i], i, path, res)
            # 回溯，撤销选择
            path.pop()

# 实例化Solution类
sol = Solution()
# 调用combinationSum函数并打印结果
print(sol.combinationSum([2,3,6,7], 7))  # 示例1
print(sol.combinationSum([2,3,5], 8))    # 示例2