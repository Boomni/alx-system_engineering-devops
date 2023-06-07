#!/usr/bin/python3
"""
2-recurse
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list containing the titles of all hot articles for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "Custom User Agent"}
    params = {"after": after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        after = data["data"]["after"]

        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        if after is not None:
            recurse(subreddit, hot_list, after)

    elif response.status_code == 404:
        return None

    return hot_list
