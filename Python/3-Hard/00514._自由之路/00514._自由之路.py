from typing import List

def findRotateSteps(ring: str, key: str) -> int:
    """
    动态规划解决自由之路问题
    
    Args:
    ring: 字符串，表示圆盘上的字母顺序
    key: 字符串，表示需要拼写的关键词
    
    Returns:
    int: 拼写整个关键词需要的最少步数
    
    """
    # 计算两点之间的最短距离
    def dist(pos1: int, pos2: int, n: int) -> int:
        """计算环形距离"""
        return min(abs(pos1-pos2), n-abs(pos1-pos2))
    
    # 预处理，记录ring中每个字母出现的所有位置
    pos_map = {}
    for i, ch in enumerate(ring):
        if ch not in pos_map:
            pos_map[ch] = []
        pos_map[ch].append(i)
    
    n = len(ring)
    m = len(key)
    # 初始化动态规划数组
    dp = [[float('inf')] * n for _ in range(m)]
    
    # 边界条件初始化
    for j in pos_map[key[-1]]:
        dp[-1][j] = min(dist(j, 0, n), dist(0, j, n)) + 1  # 加1是因为选择字符也需要一步
    
    # 动态规划，从后往前填表
    for i in range(m-2, -1, -1):  # 从倒数第二个字符开始
        for j in pos_map[key[i]]:  # 当前字符在ring中的所有位置
            for k in pos_map[key[i+1]]:  # 下一个字符在ring中的所有位置
                dp[i][j] = min(dp[i][j], dp[i+1][k] + dist(j, k, n) + 1)  # 加1是选择当前字符的步骤
    
    # 最终结果，从ring的起点开始，到拼写完key所需的最少步数
    return dp[0][0]

# 测试用例
ring = "godding"
key = "gd"
# 运行代码
steps = findRotateSteps(ring, key)
print(f"拼写'{key}'需要的最少步数是: {steps}")
