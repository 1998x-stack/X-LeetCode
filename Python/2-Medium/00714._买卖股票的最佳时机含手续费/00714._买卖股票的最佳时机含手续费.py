from typing import List

def max_profit(prices: List[int], fee: int) -> int:
    """
    计算给定股票价格和交易手续费的条件下，可以获得的最大利润。

    Args:
    prices (List[int]): 股票的价格列表。
    fee (int): 每次交易需要支付的手续费。

    Returns:
    int: 可以获得的最大利润。
    """
    if not prices:
        return 0
    
    cash, hold = 0, -prices[0]
    for price in prices[1:]:
        cash = max(cash, hold + price - fee) # 卖出股票
        hold = max(hold, cash - price) # 买入股票
    
    return cash


# 测试用例
prices = [1, 3, 2, 8, 14, 9]
fee = 2
result = max_profit(prices, fee)
print(f"最大利润为: {result}")