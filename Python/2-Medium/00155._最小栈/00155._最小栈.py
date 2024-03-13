from typing import List

class MinStack:
    def __init__(self):
        """
        初始化数据结构。主栈用于存储所有元素，辅助栈用于存储每个状态下的最小值。
        """
        self.stack = []  # 主栈
        self.min_stack = []  # 辅助栈

    def push(self, x: int) -> None:
        """
        如果辅助栈为空或新元素小于等于辅助栈顶元素，则同时将新元素压入辅助栈。
        """
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        """
        弹出主栈顶部元素，如果弹出的元素等于辅助栈顶部元素，则也弹出辅助栈顶部元素。
        """
        x = self.stack.pop()
        if x == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        """
        获取主栈顶部元素。
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """
        获取辅助栈顶部元素，即当前最小值。
        """
        return self.min_stack[-1]

# 测试代码
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print("Min:", min_stack.getMin())  # 应返回 -3
min_stack.pop()
print("Top:", min_stack.top())     # 应返回 0
print("Min:", min_stack.getMin())  # 应返回 -2