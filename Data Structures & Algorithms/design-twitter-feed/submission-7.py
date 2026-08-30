class Twitter:

    def __init__(self):

        # tweetMap: (userId, [count, tweetId])
        # followerMap: (userId, {followeeId})
        # self.coint: tracks the time at which the tweet was added to the tweetMap
        self.tweetMap = defaultdict(list)
        self.followerMap = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # make a copy of the list not reference
        tweets = list(self.tweetMap[userId])

        for followeeId in self.followerMap[userId]:
            tweets.extend(self.tweetMap[followeeId])
        
        max_heap = []
        heapq.heapify(max_heap)
        for tweet in tweets: 
            heapq.heappush(max_heap, tweet)
            if len(max_heap) > 10:
                heapq.heappop(max_heap)
        
        res = []
        for count, tweet in sorted(max_heap, reverse=True):
            res.append(tweet)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followerMap and followeeId in self.followerMap[followerId]: 
            self.followerMap[followerId].remove(followeeId)
        
