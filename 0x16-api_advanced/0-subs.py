#!/usr/bin/python3
'''number of subscribers for a given subreddit'''
import requests


def number_of_subscribers(subreddit):
    headers = {'User-agent': 'Hachem'}
    try:
        r = requests.get(
            'https://www.reddit.com/r/{}/about.json'.format(subreddit),
            headers=headers)
        data = r.json()
        return(data.get('data').get('subscribers'))
    except AttributeError:
        return 0
