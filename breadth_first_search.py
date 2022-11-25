# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 14:45:44 2022

@author: shi-n
"""

from collections import deque


def person_is_target(name):
    return name[-1] == 'm'


def breadth_first_search(graph: dict, start: str, target_function=person_is_target) -> list[str]:
    search_queue = deque()
    search_queue += graph[start]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if target_function(person):
                print(person + ' is the target')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


if __name__ == '__main__':
    graph = {}
    graph['you'] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []

    breadth_first_search(graph, 'you', target_function=person_is_target)
