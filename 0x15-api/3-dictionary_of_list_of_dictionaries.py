#!/usr/bin/python3
""" Dictionary of list of dictionaries"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    req1 = requests.get(url="https://jsonplaceholder.typicode.com/todos")
    req2 = requests.get(url="https://jsonplaceholder.typicode.com/users")
    todos = req1.json()
    users = req2.json()
    dictionary = {}
    with open('todo_all_employees' + '.json', mode='w') as nf:
        for items in user:
            USERNAME = items.get("username")
            ID = items.get("id")
            dictionary[ID] = []
            for tasks in todo:
                if ID == tasks["userId"]:
                    data = {}
                    data = {"username": USERNAME, "task": tasks.get("title"),
                            "completed": tasks.get("completed")}
                    dictionary[ID].append(data)
        json.dump(dictionary, nf)
