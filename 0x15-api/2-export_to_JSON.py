#!/usr/bin/python3
""" Export to JSON"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    U_ID = {'userId': argv[1]}
    ID = {'id': argv[1]}
    req1 = requests.get(
        url="https://jsonplaceholder.typicode.com/todos",
        params=U_ID)
    req2 = requests.get(
        url="https://jsonplaceholder.typicode.com/users",
        params=ID)
    todos = req1.json()
    users = req2.json()
    for item in users:
        USER_ID = item.get("id")
        USERNAME = item.get("username")
    new_f = str(USER_ID) + '.json'
    info = {USER_ID: []}
    with open(new_f, mode='w') as nf:
        for item in todos:
            dic = {}
            dic["task"] = item.get('title')
            dic["completed"] = item.get('completed')
            dic["username"] = USERNAME
            info[USER_ID].append(dic)
        json.dump(info, nf)
