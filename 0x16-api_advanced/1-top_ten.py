#!/usr/bin/python3
"""
Function queries the Reddit API and prints the titles of the first 10 hot posts listed 
"""
import requests


def top_ten(subreddit):
    """ Returns: top ten post titles
        or None if queried subreddit is invalid
    """
    headers = {'User-Agent': 'ekan777'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        titles = response.json().get('data').get('children')
        for title in titles:
            print(title.get('data').get('title'))
    else:
        print(None)
