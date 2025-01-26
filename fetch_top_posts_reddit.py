import os
import requests
from datetime import datetime
import json

# Function to fetch top posts from a subreddit
def fetch_top_reddit_posts(subreddit, limit=5):
    url = f"https://www.reddit.com/r/{subreddit}/top.json?t=day&limit={limit}"
    headers = {'User-Agent': 'PythonRedditBot/0.1'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = [
            f"Title: {post['data']['title']}\nURL: https://www.reddit.com{post['data']['permalink']}\n"
            for post in data['data']['children']
        ]
        return posts
    else:
        return [f"Error fetching posts. Status code: {response.status_code}"]

# Function to save the posts to a text file
def save_to_file(posts, subreddit):
    if not posts:
        print("No posts to save.")
        return
    
    # Create a directory to store the files
    if not os.path.exists("reddit_summaries"):
        os.makedirs("reddit_summaries")
    
    filename = f"reddit_summaries/{subreddit}_daily_summary_{datetime.now().strftime('%Y-%m-%d')}.txt"
    with open(filename, 'w') as file:
        file.write(f"Daily Summary of r/{subreddit} - {datetime.now().strftime('%Y-%m-%d')}\n")
        file.write("=" * 50 + "\n\n")
        file.write("\n\n".join(posts))
    
    print(f"Summary saved to {filename}")

# Main logic
if __name__ == "__main__":
    subreddit = input("Enter the subreddit you want to fetch posts from:")
    # subreddit = str(input())
    # subreddit = "CreditCards"  # Change this to any subreddit you like
    if not subreddit:
        print("Subreddit cannot be empty!")
        exit()
    else:
        top_posts = fetch_top_reddit_posts(subreddit)
        save_to_file(top_posts, subreddit)


# def lambda_handler(event, context):
#     subreddit = event.get("subreddit", "CreditCards")  # Default subreddit
#     if not subreddit:
#         return {"statusCode": 400, "body": "Subreddit cannot be empty!"}

#     posts = fetch_top_reddit_posts(subreddit)
#     return {
#         "statusCode": 200,
#         "body": json.dumps(posts)
#     }
