from typing import List

def h_index(citations: List[int]) -> int:
    """
    计算研究者的H指数。
    
    Args:
    citations: List[int] - 研究者每篇论文的引用次数列表。
    
    Returns:
    int - 研究者的H指数。
    
    示例:
    >>> h_index([3,0,6,1,5])
    3
    """
    # 对引用次数进行降序排序
    citations.sort(reverse=True)
    
    # 线性扫描，找到满足条件的最大索引 i
    h_idx = 0  # 初始化H指数
    for i, citation in enumerate(citations):
        if citation >= i + 1:  # 检查是否至少有i+1篇论文引用次数≥i+1
            h_idx = i + 1  # 更新H指数
        else:
            break  # 一旦不满足条件，即可终止循环
    
    return h_idx

# 测试代码
test_citations = [3,0,6,1,5]
h_index_value = h_index(test_citations)
print(f"测试案例 [3,0,6,1,5] 的 H 指数是: {h_index_value}")
