#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ Returns number of subscribers"""
    reddit_url = "https://www.reddit.com/r/{}/about.json"
    url = reddit_url.format(subreddit)
    response = requests.get(
            url, headers={"User-Agent": "MyBot/1.0"}, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json()
    return data['data']['subscribers']
