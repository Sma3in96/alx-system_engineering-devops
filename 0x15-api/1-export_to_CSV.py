#!/usr/bin/python3
"""   get data from an API """

import csv
import json
import requests
from sys import argv


def getname(id):
    ''' get user name '''
    x = requests.get("/".join([url, "users"]))
    data = json.loads(x.content)
    for d in data:
        if d.get('id') == id:
            return d.get('username')


def gettask(user_id):
    """ get task infos """
    tasks_list = []
    y = requests.get("/".join([url, "todos"]))
    data = json.loads(y.content)
    for d in data:
        if d.get('userId') == user_id:
            tasks_list.append((d.get('title'), d.get('completed')))
    return tasks_list


if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com/'

    if len(argv) == 2:
        with open(f"{argv[1]}.csv", 'a') as file:
            writer = csv.writer(file, delimiter=",", quoting=csv.QUOTE_ALL)
            for task in gettask(int(argv[1])):
                writer.writerow([str(argv[1]), getname(int(argv[1])),
                                task[1], task[0]])
