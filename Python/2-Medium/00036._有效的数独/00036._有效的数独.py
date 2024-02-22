def isValidSudoku(board: List[List[str]]) -> bool:
    """
    验证给定的9x9数独是否有效。
    
    Args:
    board: 一个列表的列表，代表9x9的数独。
    
    Returns:
    bool: 如果数独有效，则返回True；否则返回False。
    """
    # 初始化行、列和子数独的哈希表
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            # 跳过空白格子
            if num == '.':
                continue
            
            # 检查行是否有效
            if num in rows[i]:
                return False
            rows[i].add(num)
            
            # 检查列是否有效
            if num in cols[j]:
                return False
            cols[j].add(num)
            
            # 检查3x3子数独是否有效
            box_index = (i // 3) * 3 + j // 3
            if num in boxes[box_index]:
                return False
            boxes[box_index].add(num)
    
    # 所有检查都通过，返回True
    return True
