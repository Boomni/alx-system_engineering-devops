#!/usr/bin/python3
"""Module for task 2"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Queries the Reddit API and returns all hot posts
    of the subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"count": count, "after": after}
    headers = {"User-Agent": "Custom User Agent"}
    response = requests.get(url,
                            params=params,
                            headers=headers,
                            allow_redirects=False)
    if sub_info.status_code >= 400:
        return None

    hot_l = hot_list + [child.get("data").get("title")
                        for child in response.json()
                        .get("data")
                        .get("children")]

    info = response.json()
    if not info.get("data").get("after"):
        return hot_l

    return recurse(subreddit, hot_l, info.get("data").get("count"),
                   info.get("data").get("after"))
