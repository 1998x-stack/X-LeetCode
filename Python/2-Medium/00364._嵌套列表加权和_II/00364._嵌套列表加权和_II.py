from typing import List


class NestedInteger:
    """
    这是一个用于本题解的模拟 NestedInteger 类的实现，
    它能够表示整数或者一个 NestedInteger 列表。
    """
    def __init__(self, value=None):
        if isinstance(value, int):
            self._value = value
            self._list = None
        elif isinstance(value, list):
            self._list = [NestedInteger(x) for x in value]
            self._value = None
        else:
            self._value = None
            self._list = None

    def isInteger(self) -> bool:
        return self._value is not None

    def getInteger(self) -> int:
        return self._value

    def getList(self) -> List['NestedInteger']:
        # 确保总是返回一个列表
        return self._list if self._list is not None else []

def depthSumInverse(nestedList: List[NestedInteger]) -> int:
    """
    计算嵌套列表的加权和，权重为元素的反深度。

    Args:
    nestedList: List[NestedInteger]: 输入的嵌套列表

    Returns:
    int: 加权和

    """

    def findMaxDepth(nestedList: List[NestedInteger], currentDepth: int) -> int:
        """
        计算嵌套列表的最大深度。
        """
        maxDepth = currentDepth
        for ni in nestedList:
            if not ni.isInteger():
                maxDepth = max(maxDepth, findMaxDepth(ni.getList(), currentDepth + 1))
        return maxDepth

    def dfs(nestedList: List[NestedInteger], currentDepth: int, maxDepth: int) -> int:
        """
        递归计算每个整数的加权和。
        """
        total = 0
        for ni in nestedList:
            if ni.isInteger():
                # 使用最大深度和当前深度来计算权重
                total += ni.getInteger() * (maxDepth - currentDepth + 1)
            else:
                total += dfs(ni.getList(), currentDepth + 1, maxDepth)
        return total

    maxDepth = findMaxDepth(nestedList, 1)
    return dfs(nestedList, 1, maxDepth)

# 重新运行测试用例
test_case_1 = [NestedInteger([1,1]), NestedInteger(2), NestedInteger([1,1])]
test_case_2 = [NestedInteger(1), NestedInteger([4, NestedInteger([6])])]

# 运行代码
print(depthSumInverse(test_case_1))  # 应输出 8
print(depthSumInverse(test_case_2))  # 应输出 17