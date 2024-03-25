from typing import List

class NestedInteger:
    def __init__(self, value=None):
        self.value = value if value is not None else []
    
    def isInteger(self) -> bool:
        return isinstance(self.value, int)

    def add(self, elem):
        if isinstance(self.value, list):
            self.value.append(elem)
        else:
            raise ValueError("当前NestedInteger不是列表")

    def setInteger(self, value: int):
        self.value = value
    
    def getInteger(self) -> int:
        if self.isInteger():
            return self.value
        else:
            raise ValueError("当前NestedInteger不是整数")
    
    def getList(self) -> [List['NestedInteger']]:
        if not self.isInteger():
            return self.value
        else:
            raise ValueError("当前NestedInteger不是列表")

class NestedIterator:
    def __init__(self, nestedList: [List[NestedInteger]]):
        self.stack = nestedList[::-1]  # 将嵌套列表反向压入栈中

    def next(self) -> int:
        # 返回栈顶元素的整数值
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        # 检查是否还有下一个元素
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False

# 创建NestedInteger示例
nestedList = [NestedInteger([NestedInteger(1), NestedInteger(1)]), NestedInteger(2), NestedInteger([NestedInteger(1), NestedInteger(1)])]

# 初始化迭代器
iterator = NestedIterator(nestedList)

# 遍历迭代器，并打印每个元素
while iterator.hasNext():
    print(iterator.next(), end=' ')