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

    b_url = 'https://www.reddit.com/r/'
    header = {"User-Agent": "MyCustomUserAgent/1.0"}
    get_url = '{}{}/about.json'.format(b_url, subreddit)
    results = requests.get(
        get_url,
        headers=header,
        allow_redirects=False
    )
    if results.status_code == 200:
        return results.json()['data']['subscribers']
    return 0