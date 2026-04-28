import heapq


class Tweet:
    def __init__(self, tweet_id, timestamp):
        self.tweet_id = tweet_id
        self.timestamp = timestamp


class Twitter:
    def __init__(self):
        self.user_tweets = {}  # User ID -> List of Tweet objects
        self.user_followees = {}  # User ID -> Set of followees
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        self.user_tweets[userId].append(Tweet(tweetId, self.timestamp))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []

        if userId in self.user_tweets:
            tweets.extend(self.user_tweets[userId])

        if userId in self.user_followees:
            for followee in self.user_followees[userId]:
                if followee in self.user_tweets:
                    tweets.extend(self.user_tweets[followee])

        tweets.sort(key=lambda x: x.timestamp, reverse=True)
        return [tweet.tweet_id for tweet in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId not in self.user_followees:
                self.user_followees[followerId] = set()
            self.user_followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (
            followerId in self.user_followees
            and followeeId in self.user_followees[followerId]
        ):
            self.user_followees[followerId].remove(followeeId)
