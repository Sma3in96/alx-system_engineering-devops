#!/usr/bin/python3
"""Module that consumes the Reddit API,
titles of all hot articles for a given subreddit."""
import requests


def top_ten(subreddit):
    """A function that queries the Reddit API,
    And prints the titles of the first 10,
    Hot posts listed for a specified subreddit."""
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
        headers={"User-Agent": "costum"}
    )
    if response.status_code == 200:
        for item in response.json()["data"]["children"]:
            print(item["data"]["title"])
    else:
        print(None)
