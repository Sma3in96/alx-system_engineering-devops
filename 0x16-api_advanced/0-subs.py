#!/usr/bin/python3
"""Module that consumes the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """return number of subs in an existing account
    subreddit is the target
     Args:
        subreddit (str): subreddit

    Returns:
        int: number of subscribers
        """
    header = {"User-Agent": "custom"}
    get_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    results = requests.get(
        get_url,
        headers=header,
        allow_redirects=False
    )
    if results.status_code == 200:
        return results.json()['data']['subscribers']
    return 0
