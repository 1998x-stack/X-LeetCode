from typing import List

class Vector2D:
    def __init__(self, vec: List[List[int]]):
        """
        初始化二维向量迭代器。

        Args:
            vec: 二维整数向量。

        """
        self.vec = vec
        self.row = 0  # 行指针
        self.col = 0  # 列指针

    def next(self) -> int:
        """
        返回二维向量的下一个元素。

        Returns:
            下一个整数元素。

        """
        # 如果当前位置不合法，则移动到下一个合法位置
        if not self.hasNext():
            return None  # 或抛出异常
        result = self.vec[self.row][self.col]
        self.col += 1  # 移动到下一个元素
        return result

    def hasNext(self) -> bool:
        """
        检查二维向量中是否还有下一个元素。

        Returns:
            如果存在下一个元素，则返回 True；否则返回 False。

        """
        while self.row < len(self.vec):
            if self.col < len(self.vec[self.row]):
                return True
            self.row += 1
            self.col = 0
        return False

# 测试代码
vector = [[1, 2], [3], [4]]
v = Vector2D(vector)
print(v.next())  # 输出 1
print(v.next())  # 输出 2
print(v.next())  # 输出 3
print(v.hasNext())  # 输出 True
print(v.next())  # 输出 4
print(v.hasNext())  # 输出 False