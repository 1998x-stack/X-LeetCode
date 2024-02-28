# 重新定义之前提到的函数和类，因为代码执行状态已重置

def removeConsecutiveBalls(board: str) -> str:
    """
    移除板上连续三个或更多相同颜色的球，并返回处理后的球序列。
    :param board: 当前的球序列
    :return: 处理后的球序列
    """
    i = 0
    while i < len(board):
        j = i
        while j < len(board) and board[j] == board[i]:
            j += 1
        if j - i >= 3:
            return removeConsecutiveBalls(board[:i] + board[j:])
        i = j
    return board

class ZumaGame:
    def __init__(self):
        self.memo = {}  # 用于记忆化的存储

    def findMinStep(self, board: str, hand: str) -> int:
        hand = ''.join(sorted(hand))  # 对手中的球进行排序
        result = self.dfs(board, hand)  # 开始深度优先搜索
        return result if result != float('inf') else -1

    def dfs(self, board: str, hand: str) -> int:
        if not board:  # 如果板上没有球了
            return 0
        if (board, hand) in self.memo:  # 如果这个状态已经计算过
            return self.memo[(board, hand)]
        
        minStep = float('inf')
        for i in range(len(hand)):
            for j in range(len(board) + 1):
                new_board = board[:j] + hand[i] + board[j:]
                new_board = removeConsecutiveBalls(new_board)
                if new_board != board:
                    next_hand = hand[:i] + hand[i+1:]
                    steps = 1 + self.dfs(new_board, next_hand)
                    minStep = min(minStep, steps)
        
        self.memo[(board, hand)] = minStep
        return minStep

# 测试 ZumaGame 类
zuma_game = ZumaGame()
test_cases = [
    ("WRRBBW", "RB"),
    ("WWRRBBWW", "WRBRW"),
    ("G", "GGGGG")
]

results = [zuma_game.findMinStep(board, hand) for board, hand in test_cases]
print(results)  # [2, 2, -1]