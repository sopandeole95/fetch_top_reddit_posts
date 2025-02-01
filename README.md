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

Automating with Windows Task Scheduler
You can set up Windows Task Scheduler to run this script automatically at a scheduled time.

Steps to Set Up Automation
    Open Task Scheduler
        Press Win + R, type taskschd.msc, and hit Enter.
        
    Create a New Task
        Click "Create Basic Task" and name it (e.g., "Reddit Fetcher").

    Set a Trigger (Schedule)
        Choose Daily (or your preferred frequency).
        Set the time (e.g., 9:00 AM every day).
    
    Set the Action
        Select "Start a Program".
        In "Program/Script", enter the path to python.exe: 
            C:\Python39\python.exe
        In "Add arguments", enter the full path to your script:
            C:\Users\YourName\fetch_top_posts_reddit.py
    
    Finish and Enable Task
        Click Finish.
        In Task Scheduler Library, right-click your task and click Run to test.

Now, your script will run automatically at the scheduled time!