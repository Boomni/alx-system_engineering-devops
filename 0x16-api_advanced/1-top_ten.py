#!/usr/bin/python3
"""
function that queries the Reddit API and
prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    if subreddit is None or type(subreddit) is not str:
        print('None')
        return

    base_url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}
    r = requests.get(base_url, headers=headers, allow_redirects=False).json()

    if r.get('data') is None:
        print('None')
        return

    i = 0
    data = r.get('data').get('children')

    for i in range(0, 10):
        print(data[i].get('data').get('title'))
        i += 1
