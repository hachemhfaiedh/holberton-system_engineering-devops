#!/usr/bin/python3
""" Gather data from an API"""
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

    td = 0
    for task in todos:
        if task.get("completed"):
            td += 1
    for i in user:
        name = i.get("name")
    print("Employee {} is done with tasks({}/{}):".format(
        name, td, len(todos)))
    for task in todos:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))
