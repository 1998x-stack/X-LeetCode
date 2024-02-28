from typing import List
import heapq  # 用于实现最大堆和最小堆

class SlidingWindowMedian:
    def __init__(self):
        # 初始化两个堆：最大堆和最小堆
        self.max_heap = []  # 存放窗口较小一半的元素，Python中通过插入元素的相反数来实现最大堆
        self.min_heap = []  # 存放窗口较大一半的元素

    def rebalance_heaps(self):
        """平衡两个堆，确保两个堆的大小差不超过1"""
        # 如果最大堆的大小超过最小堆的大小超过1，移动最大堆的顶部元素到最小堆
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        # 如果最小堆的大小超过最大堆的大小，移动最小堆的顶部元素到最大堆
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def add_num(self, num: int):
        """向窗口中添加一个数，并保持堆平衡"""
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        self.rebalance_heaps()

    def remove_num(self, num: int):
        """从窗口中移除一个数，并保持堆平衡"""
        if num <= -self.max_heap[0]:
            self.max_heap.remove(-num)
            heapq.heapify(self.max_heap)
        else:
            self.min_heap.remove(num)
            heapq.heapify(self.min_heap)
        self.rebalance_heaps()

    def find_median(self) -> float:
        """找到当前窗口的中位数"""
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        elif len(self.max_heap) < len(self.min_heap):
            return self.min_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2

    def median_sliding_window(self, nums: List[int], k: int) -> List[float]:
        """计算并返回每个窗口的中位数"""
        result = []
        for i in range(len(nums)):
            self.add_num(nums[i])
            if i >= k - 1:
                result.append(self.find_median())
                self.remove_num(nums[i - k + 1])
        return result

# 示例代码运行
if __name__ == "__main__":
    solution = SlidingWindowMedian()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(solution.median_sliding_window(nums, k))