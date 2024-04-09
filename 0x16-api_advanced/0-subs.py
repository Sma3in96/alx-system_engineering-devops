#!/usr/bin/python3
"""Return How many subs."""

import requests
import json

redit_url = 'https://www.reddit.com/r/'


def number_of_subscribers(subreddit):
    """Return number of subs."""

    url = f"{redit_url}/{subreddit}/about.json"

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    results = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )
    if results.status_code == 200:
        return results.json()['data']['subscribers']
    return 0
