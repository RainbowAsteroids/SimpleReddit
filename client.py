"""
SimpleReddit
Very simple Reddit client to learn the Reddit API
By Dylan Hamer
"""

import praw  # Reddit API

"""OAuth credentials: Remove these before commiting to source control"""
id = "ENTER CLIENT ID"
secret = "ENTER CLIENT SECRET"
agent = "SimpleReddit (by /u/dylanhamer13)"

class simpleReddit:
    def __init__(self):
        """Initialise Reddit instance"""
        self.reddit = praw.Reddit(user_agent=agent,
                             client_secret=secret,
                             client_id=id)
        self.subreddit = "news"
        self.sort = "hot"

    def browse(self, showScores = True):
        """View posts"""
        subreddit = self.reddit.subreddit(self.subreddit)
        posts = getattr(subreddit, self.sort)()  # Get posts in subreddit
        for post in posts:
            print(post.title)
            print(getattr(post, "body", "-"))
            if showScores:
                print(dir(post))
            print("-"*40)

simpleReddit = simpleReddit()
simpleReddit.browse()
