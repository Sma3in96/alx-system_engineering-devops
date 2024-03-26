#!/usr/bin/python3
"""   get data from an API """

import json
import requests


def getids():
    ''' get user name '''
    ids_list = list()
    x = requests.get("/".join([url, "users"]))
    data = json.loads(x.content)
    for d in data:
        ids_list.append(d.get('id'))
    return ids_list


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
            tasks_list.append({"username": username,
                               "task": d.get('title'),
                               "completed": d.get('completed')})
    return tasks_list


if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com/'
    dict_user_todo = dict()

    with open("todo_all_employees.json", 'a', encoding="utf-8") as file:
        for id in getids():
            dict_user_todo[str(id)] = gettask(int(id))
        json.dump(dict_user_todo, file)
        
