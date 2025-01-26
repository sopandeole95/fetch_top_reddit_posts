# Fetch Top Reddit Posts

This repository contains a Python script that fetches the top daily posts from a specified subreddit using the Reddit API. The fetched posts are saved to a local text file for convenient daily summaries.

---

## Features

- Fetches top daily posts (title and URL) from any subreddit.
- Saves posts in a readable text file with a timestamp.
- Designed for deployment on **AWS Lambda** for automated execution.

---

## Dependencies

This script requires Python 3.x and the following Python libraries:
- `requests`

Install dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt

-----------------How to Use------------------
Running Locally
    Clone the repository:
    git clone https://github.com/<your-username>/<folder_name>.git
    cd folder_name

Install dependencies:
    pip install -r requirements.txt

Run the script:
    python fetch_top_posts_reddit.py

The script will:

    Fetch the top posts from the inputed subreddit.
    Save them to a text file.


-----------------Deploying on AWS Lambda------------------
Package the script and dependencies into a .zip file:
    pip install requests -t .
    zip -r python_script_name.zip .

Upload the .zip file to AWS Lambda.

Set the handler to:
    <python_script_name>.lambda_handler

Test with a payload:
    {
    "subreddit": "python" ##for testing, we can choose any subreddit
}
