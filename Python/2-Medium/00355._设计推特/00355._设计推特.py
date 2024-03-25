from typing import List, Dict, Set
import heapq

class Twitter:
    def __init__(self):
        # 初始化用户推文映射和用户关注列表
        self.user_tweets: Dict[int, List[int]] = {}
        self.user_follows: Dict[int, Set[int]] = {}
        self.tweet_time: Dict[int, int] = {}  # 推文ID映射到时间戳
        self.time = 0  # 全局时间戳

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 发布推文，记录时间戳
        self.time += 1  # 更新时间戳
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        self.user_tweets[userId].append(tweetId)
        self.tweet_time[tweetId] = self.time

    def getNewsFeed(self, userId: int) -> List[int]:
        # 获取新闻推送，包括自己和关注的人的最新10条推文
        news_feed = []
        min_heap = []  # 使用小根堆存储推文（时间戳，推文ID）
        follows = self.user_follows.get(userId, set())
        if userId not in follows:
            follows.add(userId)  # 包括自己的推文
        
        for user in follows:
            tweets = self.user_tweets.get(user, [])
            for tweetId in tweets[-10:]:  # 只考虑最新的10条推文
                heapq.heappush(min_heap, (self.tweet_time[tweetId], tweetId))
                if len(min_heap) > 10:  # 保持堆的大小不超过10
                    heapq.heappop(min_heap)
        
        while min_heap:
            news_feed.insert(0, heapq.heappop(min_heap)[1])  # 按时间戳逆序插入
        
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # 关注用户
        if followerId not in self.user_follows:
            self.user_follows[followerId] = set()
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # 取消关注用户
        if followerId in self.user_follows and followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId)

# 实例化Twitter类，并运行示例
twitter = Twitter()
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))  # 预期输出: [5]
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))  # 预期输出: [6, 5]
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))  # 预期输出: [5]