from typing import List

def solve(board: List[List[str]]) -> None:
    """
    采用 DFS 算法修改被 'X' 围绕的区域。
    
    Args:
    - board: List[List[str]], 二维字符数组，代表棋盘。
    
    Returns:
    None, 直接在输入的 board 上修改。
    """
    if not board or not board[0]:
        return

    m, n = len(board), len(board[0])

    def dfs(x: int, y: int) -> None:
        """
        深度优先搜索，标记与边界上 'O' 相连的 'O'。
        
        Args:
        - x: 当前行坐标。
        - y: 当前列坐标。
        """
        if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != 'O':
            return
        board[x][y] = 'A'  # 标记当前位置
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

    # 从边界开始 DFS
    for i in range(m):
        dfs(i, 0)
        dfs(i, n - 1)
    for j in range(n):
        dfs(0, j)
        dfs(m - 1, j)

    # 将 'A' 复原为 'O'，未标记的 'O' 转换为 'X'
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'A':
                board[i][j] = 'O'
            elif board[i][j] == 'O':
                board[i][j] = 'X'

# 示例棋盘
board_example = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]
solve(board_example)
board_example