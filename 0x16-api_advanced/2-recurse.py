#!/usr/bin/python3
'''list containing the titles of all hot articles for a given subreddit'''
import requests


def recurse(subreddit, hot_list=[], after=''):
    headers = {'User-agent': 'Hachem'}
    try:
        r = requests.get(
            'https://www.reddit.com/r/{}/hot.json?after={}'.
            format(subreddit, after),
            headers=headers)
        data = r.json()
        a = data.get('data')
        b = a.get('children')
        for i in b:
            hot_list.append(i.get('data').get('title'))
        after = a.get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except AttributeError:
        return None
