import praw
from os import getenv
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id = getenv("REDDIT_CLIENT"),
    client_secret = getenv("REDDIT_SECRET"),
    username = "username",
    password = "password",
    user_agent = "python",
)
reddit.read_only = True

def fetch_post(subreddit):
    submission = reddit.subreddit(subreddit).random()
    return format_reddit_post(submission)

def format_reddit_post(submission):
    return(f"> {submission.title} by {submission.author.name}. {submission.url}")
    
