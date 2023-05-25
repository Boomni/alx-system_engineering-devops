#!/usr/bin/python3
"""
Extends the 0-gather_data_from_an_API.py Python script
To export data in the CSV format instead.
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    todo = requests.get(
            'https://jsonplaceholder.typicode.com/todos/',
            params={'userId': user_id}
            ).json()
    user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'
            .format(user_id)
            ).json()
    username = user.get('username')

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        file_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [
                file_writer.writerow(
                    [
                        user_id,
                        username,
                        task.get('completed'),
                        task.get('title')
                        ]
                    ) for task in todo
         ]
