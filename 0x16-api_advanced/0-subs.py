#!/usr/bin/python3
"""
0-subs
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0


if __name__ == '__main__':
    number_of_subscribers = number_of_subscribers(sys.argv[1])
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
