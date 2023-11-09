#!/usr/bin/python3
"""
Recursive function that queries the Reddit Api
"""
import requests


def count_words(subreddit, word_list, word_counts=None, after=None):
    if word_counts is None:
        word_counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'linux:api.advanced:v3.1.0'
    }

    if after:
        url += f"?after={after}"

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        subreddit_data = response.json()
        for post in subreddit_data['data']['children']:
            title = post['data']['title'].lower()
            for word in title.split():
                cleaned_word = clean_word(word)
                if cleaned_word in word_list:
                    word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1
        after = subreddit_data['data']['after']

        if after:
            return count_words(subreddit, word_list, word_counts, after)
        else:
            sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_counts:
                print(f"{word}: {count}")
    else:
        print("Invalid subreddit or no matching words found.")
