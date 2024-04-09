#!/usr/bin/python3
"""The reddit api."""
import requests


def top_ten(subreddit):
    """Retrives the Reddit API."""
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
        headers={"User-Agent": "costum"}
    )
    if response.status_code == 200:
        for item in response.json()["data"]["children"]:
            print(item["data"]["title"])
    else:
        print(None)
