#!/usr/bin/python3
"""   get data from an API """

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
    username = getname(user_id)
    y = requests.get("/".join([url, "todos"]))
    data = json.loads(y.content)
    for d in data:
        if d.get('userId') == user_id:
            tasks_list.append({"task": d.get('title'),
                               "completed": d.get('completed'),
                               "username": username})
    return tasks_list


if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com/'

    if len(argv) == 2:
        with open(f"{argv[1]}.json", 'a', encoding="utf-8") as file:
            json.dump({str(argv[1]): gettask(int(argv[1]))}, file)
                
