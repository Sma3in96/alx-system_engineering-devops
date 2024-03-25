#!/usr/bin/python3
"""   get data from an API """

import json
from sys import argv
import requests


def getname(id):
    ''' get user name '''
    x = requests.get("/".join([url, "users"]))
    data = json.loads(x.content)
    for d in data:
        if d.get('id') == id:
            return d.get('name')


def gettask(user_id):
    """ get task infos """
    number_tasks_done = 0
    number_tasks = 0
    list_titles = list()
    y = requests.get("/".join([url, "todos"]))
    data = json.loads(y.content)
    for d in data:
        if d.get('userId') == user_id:
            number_tasks = number_tasks + 1
            if d.get('completed'):
                number_tasks_done = number_tasks_done + 1
                list_titles.append(d.get('title'))
    return [number_tasks_done, number_tasks, list_titles]


if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com/'

    if len(argv) == 2:
        NUMBER_OF_DONE_TASKS = gettask(int(argv[1]))[0]
        TOTAL_NUMBER_OF_TASKS = gettask(int(argv[1]))[1]
        EMPLOYEE_NAME = getname(int(argv[1]))
        print(f"Employee {EMPLOYEE_NAME} is done with tasks"
              f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
        for title in gettask(int(argv[1]))[2]:
            print(f"\t {title}")
