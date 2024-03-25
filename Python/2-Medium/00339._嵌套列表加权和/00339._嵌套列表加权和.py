from typing import List, Union

# 定义嵌套列表的类型
NestedInteger = Union[int, List['NestedInteger']]

def nestedListWeightSum(nestedList: List[NestedInteger]) -> int:
    """
    计算嵌套列表的加权和。

    Args:
    nestedList: List[NestedInteger]: 一个嵌套的整数列表。
    
    Returns:
    int: 加权和。
    
    示例:
    >>> nestedListWeightSum([[1,1],2,[1,1]])
    10
    >>> nestedListWeightSum([1,[4,[6]]])
    27
    """
    
    def dfs(element: NestedInteger, depth: int) -> int:
        """
        深度优先搜索计算加权和。
        
        Args:
        element: NestedInteger: 当前处理的元素，可以是整数也可以是列表。
        depth: int: 当前深度。
        
        Returns:
        int: 当前元素的加权和。
        """
        if isinstance(element, int):
            # 如果是整数，直接返回该整数乘以其深度
            return element * depth
        else:
            # 如果是列表，递归计算每个元素的加权和并累加
            return sum(dfs(e, depth + 1) for e in element)
    
    # 对于嵌套列表的每个元素进行深度优先搜索，初始深度为1
    return sum(dfs(element, 1) for element in nestedList)

# 示例测试
test_cases = [
    ([[1,1],2,[1,1]], 10),  # 示例 1
    ([1,[4,[6]]], 27),      # 示例 2
]

# 执行测试
for nestedList, expected in test_cases:
    result = nestedListWeightSum(nestedList)
    print(f"nestedList: {nestedList}, Expected: {expected}, Got: {result}")