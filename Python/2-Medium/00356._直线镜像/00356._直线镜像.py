from typing import List, Tuple


def isReflected_fixed(points: List[Tuple[int, int]]) -> bool:
    # 确保输入点都转换为元组形式，以避免 TypeError
    points_set = set(map(tuple, points))  # 转换为元组的集合，以确保可哈希

    max_x = max(x for x, y in points_set)
    min_x = min(x for x, y in points_set)
    mirror_line_x = (max_x + min_x) / 2

    # 检查每个点是否有对应的镜像点
    for x, y in points_set:
        if (2 * mirror_line_x - x, y) not in points_set:
            return False
    return True

# 运行示例和测试代码的正确性
test_cases = [
    ([[1, 1], [-1, 1]], True),
    ([[1, 1], [-1, -1]], False),
    ([[0, 0]], True),  # 单点情况
    ([[1, 1], [1, 1], [-1, 1]], True),  # 包含重复点
]

# 重新运行修正后的测试案例
for points, expected in test_cases:
    # 确保输入是元组形式的点集
    result = isReflected_fixed(points)
    print(f"Points: {points}, Expected: {expected}, Result: {result}, Test: {'Passed' if result == expected else 'Failed'}")