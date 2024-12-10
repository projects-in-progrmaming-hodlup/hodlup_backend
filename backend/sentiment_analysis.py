import os
import praw
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def fetch_reddit_comments_with_sentiment(subreddit_name="cryptocurrency", limit_posts=5, limit_comments=5):
    """
    Fetch Reddit posts and comments with sentiment analysis.
    """
    # Load Reddit API credentials from environment variables
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

    subreddit = reddit.subreddit(subreddit_name)
    print(f"Fetching posts from r/{subreddit_name}...")

    posts_data = []
    posts = subreddit.hot(limit=limit_posts)

    for post in posts:
        post_data = {
            "title": post.title,
            "url": post.url,
            "score": post.score,
            "num_comments": post.num_comments,
            "comments": []
        }

        # Fetch comments for the post
        post.comments.replace_more(limit=0)  # Load all comments
        comments = post.comments.list()

        for comment in comments[:limit_comments]:
            # You can call the analyze_sentiment function here if needed
            sentiment = "Sentiment placeholder"  # Replace with actual analysis
            post_data["comments"].append({
                "author": str(comment.author),
                "body": comment.body,
                "sentiment": sentiment
            })

        posts_data.append(post_data)

    return posts_data
