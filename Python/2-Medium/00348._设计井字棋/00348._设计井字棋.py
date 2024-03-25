from typing import List

class TicTacToe:
    def __init__(self, n: int):
        """
        初始化一个大小为 n 的井字棋游戏板。
        """
        self.n = n
        self.rows = [[0] * n for _ in range(2)]  # 每一行的玩家1和玩家2的棋子计数
        self.cols = [[0] * n for _ in range(2)]  # 每一列的玩家1和玩家2的棋子计数
        self.diagonal = [0] * 2  # 对角线上的玩家1和玩家2的棋子计数
        self.anti_diagonal = [0] * 2  # 反对角线上的玩家1和玩家2的棋子计数

    def move(self, row: int, col: int, player: int) -> int:
        """
        玩家在(row, col)位置放置一个棋子，并检查是否胜利。
        """
        idx = player - 1  # 玩家索引，玩家1为0，玩家2为1
        
        # 更新行、列、对角线和反对角线上的计数
        self.rows[idx][row] += 1
        self.cols[idx][col] += 1
        if row == col:
            self.diagonal[idx] += 1
        if row + col == self.n - 1:
            self.anti_diagonal[idx] += 1
        
        # 检查是否满足胜利条件
        if (self.rows[idx][row] == self.n or
            self.cols[idx][col] == self.n or
            self.diagonal[idx] == self.n or
            self.anti_diagonal[idx] == self.n):
            return player
        
        return 0

# 实例化井字棋游戏并进行几次移动来验证实现
tic_tac_toe = TicTacToe(3)
moves = [(0, 0, 1), (0, 2, 2), (2, 2, 1), (1, 1, 2), (2, 0, 1), (1, 0, 2), (2, 1, 1)]
results = [tic_tac_toe.move(row, col, player) for row, col, player in moves]
print(results)  # [0, 0, 0, 0, 0, 0, 1]