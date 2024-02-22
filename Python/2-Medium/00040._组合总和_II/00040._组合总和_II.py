from typing import List

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    """
    寻找所有唯一组合，这些组合中数字的和等于给定目标数 target，每个数字在每个组合中只能使用一次。
    
    Args:
    candidates: List[int] - 候选数字的列表
    target: int - 目标数值
    
    Returns:
    List[List[int]] - 所有可能的组合，这些组合的和为目标数 target
    """
    # 初始化结果列表
    results = []
    # 对候选数字进行排序，以方便剪枝和避免重复组合
    candidates.sort()

    def backtrack(start: int, path: List[int], target: int):
        """
        使用回溯法找到所有符合条件的组合
        
        Args:
        start: int - 开始的索引
        path: List[int] - 当前路径，即已经选择的数字组合
        target: int - 调整后的目标数（减去已选择数字的和）
        """
        # 如果目标数为0，说明找到了一个有效组合，将其添加到结果列表中
        if target == 0:
            results.append(path.copy())
            return
        for i in range(start, len(candidates)):
            # 如果当前数字大于目标数，或者与前一个数字相同（避免重复），则跳过
            if candidates[i] > target or (i > start and candidates[i] == candidates[i-1]):
                continue
            # 否则，继续递归探索，注意新的目标数为 target - candidates[i]
            backtrack(i + 1, path + [candidates[i]], target - candidates[i])

    # 从第0个元素开始递归探索
    backtrack(0, [], target)
    return results

# 测试代码
candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum2(candidates, target))  # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]