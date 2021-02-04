#!/usr/bin/python3
'''titles of the first 10 hot posts listed for a given subreddit'''
import requests


def top_ten(subreddit):
    headers = {'User-agent': 'Hachem'}
    try:
        r = requests.get(
            'https://www.reddit.com/r/{}/hot.json'.format(subreddit),
            headers=headers)
        data = r.json()
        tp = data.get('data').get('children')
        for i in range(0, 10):
            print(tp[i].get('data').get('title'))
    except AttributeError:
        print(None)
