#!/usr/bin/python3
""" Export to CSV"""
import csv
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
    new_file = str(USER_ID) + ".csv"
    with open(new_file, mode='w') as nf:
        d = csv.writer(nf, delimiter=',', quoting=csv.QUOTE_ALL)
        for tasks in todos:
            TASK_STATUS = tasks.get("completed")
            TASK_TITLE = tasks.get("title")
            d.writerow([USER_ID, USERNAME, TASK_STATUS, TASK_TITLE])
