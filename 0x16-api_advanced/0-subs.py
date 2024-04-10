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
    headers = {"User-Agent": "Mozilla/1.0"}
    get_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    results = requests.get(
        get_url,
        headers=headers,
        allow_redirects=False
    )
    if results.status_code == 200:
        data = results.json()
        return data['data']['subscribers']
    return 0
