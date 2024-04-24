from typing import List, Dict, Set, Tuple

def find_user_with_most_friends(requests: List[Tuple[int, int]]) -> Dict[int, int]:
    """
    找出拥有最多好友的用户。

    Args:
    requests (List[Tuple[int, int]]): 好友请求接受列表，每个元组包含(requester_id, accepter_id)。

    Returns:
    Dict[int, int]: 包含最多好友的用户的用户 ID 和他们的好友数量。

    示例:
    >>> find_user_with_most_friends([(1, 2), (1, 3), (2, 3), (4, 3)])
    {3: 3}
    """
    friends = {}
    for requester, accepter in requests:
        friends[requester] = friends.get(requester, set())
        friends[accepter] = friends.get(accepter, set())
        
        friends[requester].add(accepter)
        friends[accepter].add(requester)
    
    # 寻找好友最多的用户
    max_friends_count = 0
    max_friends_users = {}
    for user, user_friends in friends.items():
        friend_count = len(user_friends)
        if friend_count > max_friends_count:
            max_friends_count = friend_count
            max_friends_users = {user: friend_count}
        elif friend_count == max_friends_count:
            # 获取所有的好友最多的用户
            max_friends_users[user] = friend_count
    
    return max_friends_users

# 示例数据
requests = [(1, 2), (1, 3), (2, 3), (4, 3), (2, 1)]

# 调用函数并打印结果
result = find_user_with_most_friends(requests)
print("用户ID | 好友数量")
for user_id, friends_count in result.items():
    print(f"{user_id} | {friends_count}")