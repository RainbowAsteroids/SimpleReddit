"""
SimpleReddit
Very simple Reddit client to learn the Reddit API
By Dylan Hamer
"""

import praw  # Reddit API
import prawcore
import pyfiglet  # Optional subreddit headers

"""OAuth credentials:"""
id = ""
secret = ""
agent = "SimpleReddit"

def filter(text):
	if "r/" in text:
		return text.split("/")[1]
	else:return text

class simpleReddit:
	def __init__(self):
		"""Initialise Reddit instance"""
		self.reddit = praw.Reddit(user_agent=agent,
							 client_secret=secret,
							 client_id=id)
		self.subreddit = filter(input("What subreddit would you like to browse?\n"))
		self.sort = "hot"

	def browse(self, showScores = True):
		"""View posts"""
		try:
			subreddit = self.reddit.subreddit(self.subreddit)
			posts = getattr(subreddit, self.sort)()  # Get posts in subreddit
			pyfiglet.print_figlet("/r/{}".format(self.subreddit))
			for post in posts:
				print("-"*40)
				print(post.title)
				print(getattr(post, "selftext", "-"))
				if showScores:
					print("Score: {}".format(post.score))
				print("-"*40+"\n")
		except prawcore.exceptions.InvalidToken:
			raise prawcore.exceptions.InvalidToken("The API id and secret key pair is invalid, please input valid API keys.")

simpleReddit = simpleReddit()
simpleReddit.browse()
		
