class Twitter:

    def __init__(self):
        self.tweets = {}
        self.followings = {}
        self.tweetOrder = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[tweetId] = userId
        self.tweetOrder.append(tweetId)


    def getNewsFeed(self, userId: int) -> List[int]:
        i = len(self.tweetOrder) - 1
        posts = 0
        feed = []
        while i >= 0 and posts <= 9:
            curr = self.tweetOrder[i]
            user = self.tweets[curr]
            
            if user == userId:
                
                feed.append(self.tweetOrder[i])
                posts += 1
            elif userId in self.followings:
                if user in self.followings[userId]:
                    feed.append(self.tweetOrder[i])
                    posts += 1
            i -= 1
        return feed




        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followings:
            self.followings[followerId].add(followeeId)
        else:
            self.followings[followerId] = {followeeId}
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followings:
            if followeeId in self.followings[followerId]:
                self.followings[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)