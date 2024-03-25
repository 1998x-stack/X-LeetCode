from typing import List

class SegmentTreeNode:
    def __init__(self, start: int, end: int, sum_: int = 0):
        self.start = start  # 区间起始位置
        self.end = end  # 区间结束位置
        self.sum = sum_  # 区间和
        self.left = None  # 左子树
        self.right = None  # 右子树

class NumArray:
    def __init__(self, nums: List[int]):
        self.root = self.build_tree(nums, 0, len(nums) - 1)

    def build_tree(self, nums: List[int], start: int, end: int) -> SegmentTreeNode:
        """
        构建线段树
        """
        if start > end:
            return None
        if start == end:
            return SegmentTreeNode(start, end, nums[start])
        
        mid = (start + end) // 2
        root = SegmentTreeNode(start, end)
        root.left = self.build_tree(nums, start, mid)
        root.right = self.build_tree(nums, mid + 1, end)
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, index: int, val: int) -> None:
        """
        更新数组中的一个值，并重新计算线段树中的区间和
        """
        self.update_tree(self.root, index, val)

    def update_tree(self, node: SegmentTreeNode, index: int, val: int):
        if node.start == node.end == index:
            node.sum = val
            return
        mid = (node.start + node.end) // 2
        if index <= mid:
            self.update_tree(node.left, index, val)
        else:
            self.update_tree(node.right, index, val)
        node.sum = node.left.sum + node.right.sum

    def sumRange(self, left: int, right: int) -> int:
        """
        查询区间和
        """
        return self.sum_range(self.root, left, right)

    def sum_range(self, node: SegmentTreeNode, left: int, right: int) -> int:
        if node.start == left and node.end == right:
            return node.sum
        mid = (node.start + node.end) // 2
        if right <= mid:
            return self.sum_range(node.left, left, right)
        elif left > mid:
            return self.sum_range(node.right, left, right)
        else:
            return self.sum_range(node.left, left, mid) + self.sum_range(node.right, mid + 1, right)

# 测试代码
nums = [1, 3, 5]
obj = NumArray(nums)
print(obj.sumRange(0, 2))  # 预期输出: 9
obj.update(1, 2)
print(obj.sumRange(0, 2))  # 预期输出: 8
