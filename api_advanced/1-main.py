import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetches hot post titles from a given subreddit."""
    
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit) 
    header = {'User-Agent': 'Mozilla/5.0'} 
    param = {'after': after}
    response = requests.get(url, headers=header, params=param, allow_redirects=False)
    if response.status_code != 200:
        return None
    else:
        json_res = response.json()
        after = json_res.get('data').get('after')
        has_next = after is not None
        hot_articles = json_res.get('data').get('children')
        [hot_list.append(article.get('data').get('title')) for article in hot_articles]
        return recurse(subreddit, hot_list, after=after) if has_next else hot_list

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    hot_list = recurse(subreddit)
    if hot_list is None:
        print(None)
    else:
        for title in hot_list:
            print(title)
        json_res = response.json()
        hot_articles = json_res.get('data', {}).get('children', [])
        for article in hot_articles:
            print(article.get('data', {}).get('title', ''))