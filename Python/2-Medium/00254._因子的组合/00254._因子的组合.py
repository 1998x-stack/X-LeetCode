from typing import List

def get_factors(n: int) -> List[List[int]]:
    """
    寻找所有独特的因子组合，其乘积等于给定的 n。

    Args:
    n: 一个正整数。

    Returns:
    一个列表，包含所有独特的因子组合。
    
    示例:
    >>> get_factors(8)
    [[2, 2, 2], [2, 4]]
    """

    def backtrack(start: int, path: List[int], target: int) -> None:
        """
        递归回溯函数，用于找到所有因子组合。

        Args:
        start: 开始的因子。
        path: 当前因子组合的路径。
        target: 目标乘积值。
        """
        # 终止条件：如果目标乘积降到1，说明找到了一组有效组合
        if target == 1:
            # 需要至少两个因子组合，因此长度需大于1
            if len(path) > 1:
                result.append(path[:])
            return
        
        for i in range(start, target + 1):
            # 如果当前因子能整除目标值，尝试该因子
            if target % i == 0:
                # 添加当前因子到路径中
                path.append(i)
                # 递归调用，目标值除以当前因子
                backtrack(i, path, target // i)
                # 回溯，移除路径中的当前因子
                path.pop()

    result = []  # 存储所有可能的因子组合
    backtrack(2, [], n)  # 从因子2开始
    return result

# 测试代码
print(get_factors(8))  # [[2, 2, 2], [2, 4]]