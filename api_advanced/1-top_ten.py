#!/usr/bin/python3
"""
Module to query the Reddit API and print the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit
    """
    reddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        if data and 'children' in data:
            for post in data['children'][:10]:
                print(post['data']['title'])
        else:
            print("None")
    else:
        print("None")
