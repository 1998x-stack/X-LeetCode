from typing import List

class ArrayReader:
    """ArrayReader的模拟实现，提供get方法访问元素."""
    
    def __init__(self, arr: List[int]):
        self.arr = arr
    
    def get(self, index: int) -> int:
        """如果index在数组范围内，返回数组的值，否则返回2147483647."""
        if index < len(self.arr):
            return self.arr[index]
        else:
            return 2147483647
        


def search(reader: ArrayReader, target: int) -> int:
    """在未知大小的数组中查找target的位置."""
    index = 0
    while reader.get(index) < target:
        index = index * 2 + 1
        if reader.get(index) == 2147483647:
            break
    
    left, right = 0, index
    while left <= right:
        mid = left + (right - left) // 2
        if reader.get(mid) == target:
            return mid
        elif reader.get(mid) < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
# 创建ArrayReader实例并测试代码
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reader = ArrayReader(arr)

# 测试查找不同的目标值
targets = [5, 10, 11]
results = [search(reader, target) for target in targets]
print(results)  # [4, 9, -1]