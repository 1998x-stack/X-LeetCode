from typing import List, Dict, Optional
import collections

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

def get_importance(employees: List[Employee], id: int) -> int:
    """计算指定员工及其所有下属的重要性总和。

    Args:
        employees (List[Employee]): 员工列表，每个员工是一个 Employee 对象。
        id (int): 需要计算总重要性的员工 ID。

    Returns:
        int: 指定员工及其所有下属的重要性总和。

    Examples:
        >>> emp1 = Employee(1, 5, [2, 3])
        >>> emp2 = Employee(2, 3, [])
        >>> emp3 = Employee(3, 3, [])
        >>> get_importance([emp1, emp2, emp3], 1)
        11
    """
    # 创建员工ID到Employee对象的映射
    emp_map = {emp.id: emp for emp in employees}
    
    def dfs(employee_id: int) -> int:
        """通过深度优先搜索计算员工及其所有下属的重要性。

        Args:
            employee_id (int): 当前正在处理的员工ID。

        Returns:
            int: 当前员工及其所有下属的重要性总和。
        """
        employee = emp_map[employee_id]
        total_importance = employee.importance
        # 递归地加上所有直接下属的重要性
        for sub_id in employee.subordinates:
            total_importance += dfs(sub_id)
        return total_importance

    # 检查给定ID是否存在于员工映射中
    if id not in emp_map:
        return 0
    return dfs(id)

# 测试用例
emp1 = Employee(1, 5, [2, 3])
emp2 = Employee(2, 3, [])
emp3 = Employee(3, 3, [])
print(get_importance([emp1, emp2, emp3], 1))  # 应该输出 11