#!/usr/bin/python3
"""Contains number_of_subscribers function"""
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for a given subreddit"""
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        return RESPONSE.json().get("data").get("subscribers")

    except Exception:
        return 0
