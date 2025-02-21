#!/usr/bin/python3
"""
1-main
"""
import requests

def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'python:top_ten:v1.0 (by /u/wintermancer)'}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()

    if 'data' not in data:
        print(None)
        return

    posts = data['data']['children']

    for post in posts:
        print(post['data']['title'])