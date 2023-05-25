#!/usr/bin/python3
"""
Python script that, uses a REST API

For a given employee ID
It returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    todo_url = 'https://jsonplaceholder.typicode.com/todos/'
    users_url = 'https://jsonplaceholder.typicode.com/users/{}'
    todo = requests.get(todo_url, params={'userId': sys.argv[1]}).json()
    user = requests.get(users_url.format(sys.argv[1])).json()
    completed = [
            task.get('title') for task in todo if task.get('completed') is True
            ]
    print(
            "Employee {} is done with tasks({}/{}):"
            .format(user.get('name'), len(completed), len(todo))
            )
    [print("\t {}".format(title)) for title in completed]
