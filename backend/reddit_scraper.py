import praw
import os
from dotenv import load_dotenv

def fetch_reddit_comments(subreddit_name="cryptocurrency", limit_posts=5, limit_comments=5):
    # Set up Reddit API credentials
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
        post.comments.replace_more(limit=0)
        comments = post.comments.list()

        for comment in comments[:limit_comments]:
            post_data["comments"].append({
                "author": str(comment.author),
                "body": comment.body
            })

        posts_data.append(post_data)

    return posts_data
