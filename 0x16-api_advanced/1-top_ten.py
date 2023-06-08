#!/usr/bin/python3
"""Module: 1-top_ten"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Custom User Agent"}
    response = requests.get(url, headers=headers,
                            allow_redirects=False)
    if response.status_code >= 300:
        print('None')
    else:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"]
            print(title)
