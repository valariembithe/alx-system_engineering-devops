#!/usr/bin/python3
""" queries the Reddit API and prints the titles
of the first 10 hot posts listed
"""
import requests


def top_ten(subreddit):
    """ prints the titles pf first 10 for a subreddit """
    reddit_url = 'https://www.reddit.com/r/{}/hot.json?limit=10'
    url = reddit_url.format(subreddit)
    headers = {"User-Agent": "MyBot/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return
    data = response.json()
    posts = data['data']['children']

    for post in posts:
        print(post['data']['title'])
