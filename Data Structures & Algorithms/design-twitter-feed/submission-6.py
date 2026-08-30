class Twitter:

    def __init__(self):
        self.followMap = {}
        self.tweetMap = {}
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweetMap:
            self.tweetMap[userId].append((self.count, tweetId))
        else: 
            self.tweetMap[userId] = [(self.count, tweetId)]
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = list(self.tweetMap.get(userId, []))
        followers = self.followMap.get(userId, set())
        for followerId in followers: 
            tweets.extend(self.tweetMap.get(followerId, []))
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
        if followerId in self.followMap:
            self.followMap[followerId].add(followeeId)
        else:
            self.followMap[followerId] = {followeeId}


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)
        
