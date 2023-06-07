#!/usr/bin/python3
"""
100-count
"""

import requests


def count_words(subreddit, word_list, after=None, count_dict={}):
    """Prints a sorted count of given keywords in the titles of all hot articles for a given subreddit"""
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
            words = title.lower().split()

            for word in word_list:
                count = words.count(word.lower())
                if count > 0:
                    if word.lower() in count_dict:
                        count_dict[word.lower()] += count
                    else:
                        count_dict[word.lower()] = count

        if after is not None:
            count_words(subreddit, word_list, after, count_dict)

    elif response.status_code == 404:
        return

    if not count_dict:
        return

    sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_counts:
        print(f"{word}: {count}")
