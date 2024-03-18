from typing import Tuple

def calculate_rectangle_area(x1: int, y1: int, x2: int, y2: int) -> int:
    """
    计算矩形的面积。
    
    参数:
        x1, y1: 矩形左下角的坐标。
        x2, y2: 矩形右上角的坐标。
    
    返回:
        矩形的面积。
    """
    # 矩形的宽度和高度
    width = x2 - x1
    height = y2 - y1
    # 计算面积
    return width * height

def compute_overlap_area(A: Tuple[int, int, int, int], B: Tuple[int, int, int, int]) -> int:
    """
    计算两个矩形重叠部分的面积。
    
    参数:
        A: 矩形A的坐标，格式为(x1, y1, x2, y2)。
        B: 矩形B的坐标，格式为(x1, y1, x2, y2)。
    
    返回:
        两个矩形重叠部分的面积。
    """
    # 解包矩形A和B的坐标
    ax1, ay1, ax2, ay2 = A
    bx1, by1, bx2, by2 = B
    
    # 计算重叠部分的坐标
    overlap_x1 = max(ax1, bx1)
    overlap_y1 = max(ay1, by1)
    overlap_x2 = min(ax2, bx2)
    overlap_y2 = min(ay2, by2)
    
    # 判断是否有重叠部分
    if overlap_x1 < overlap_x2 and overlap_y1 < overlap_y2:
        # 有重叠部分，计算重叠部分的面积
        return calculate_rectangle_area(overlap_x1, overlap_y1, overlap_x2, overlap_y2)
    else:
        # 无重叠部分，返回0
        return 0

def rectangle_area(A: Tuple[int, int, int, int], B: Tuple[int, int, int, int]) -> int:
    """
    计算两个矩形覆盖的总面积。
    
    参数:
        A: 矩形A的坐标，格式为(x1, y1, x2, y2)。
        B: 矩形B的坐标，格式为(x1, y1, x2, y2)。
    
    返回:
        两个矩形覆盖的总面积。
    """
    # 计算两个矩形各自的面积
    area_a = calculate_rectangle_area(*A)
    area_b = calculate_rectangle_area(*B)
    
    # 计算重叠部分的面积
    overlap_area = compute_overlap_area(A, B)
    
    # 计算总面积
    total_area = area_a + area_b - overlap_area
    
    return total_area

# 示例输入
A = (-3, 0, 3, 4)
B = (0, -1, 9, 2)

# 计算并打印总面积
total_area = rectangle_area(A, B)
print(f"总面积: {total_area}")