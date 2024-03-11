from typing import List

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    """
    计算能否绕环路行驶一周，如果可以，返回起始加油站的索引，否则返回-1。
    
    Args:
    gas: 一个整数列表，表示每个加油站有的汽油量。
    cost: 一个整数列表，表示从当前加油站到下一个加油站的耗油量。
    
    Returns:
    int: 能够绕环路行驶一周的起始加油站索引；如果不存在这样的加油站，则返回-1。
    
    示例:
    >>> canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
    3
    >>> canCompleteCircuit([2,3,4], [3,4,3])
    -1
    """
    total_tank, curr_tank, start_station = 0, 0, 0
    
    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        curr_tank += gas[i] - cost[i]
        
        # 如果当前累计的油量小于0，意味着不能从start_station到达当前站点的下一个站点
        # 需要将起始点设为当前站点的下一个站点，并重置当前油箱的油量
        if curr_tank < 0:
            start_station = i + 1
            curr_tank = 0
            
    # 如果总油量大于等于总耗油量，则存在至少一个解
    return start_station if total_tank >= 0 else -1

# 测试代码
test_cases = [([1,2,3,4,5], [3,4,5,1,2]), ([2,3,4], [3,4,3])]
results = [canCompleteCircuit(gas, cost) for gas, cost in test_cases]
results