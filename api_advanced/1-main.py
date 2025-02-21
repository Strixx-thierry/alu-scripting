import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    params = {'limit': 10}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        print("OK")
        return
    
    json_res = response.json()
    
    hot_articles = json_res.get('data', {}).get('children', [])
    
    if not hot_articles:
        print("OK")
        return
    
    for article in hot_articles:
        print(article.get('data', {}).get('title', ''))
