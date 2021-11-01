from multiprocessing import queues
from multiprocessing.queues import Queue
from tkinter.font import names
import requests
import heapq
import multiprocessing
from queue import Queue
import threading
from threading import Thread


def get_repos(name, auth, results):
    thread_name = threading.current_thread().name
    print(f'Старт {thread_name}')
    response_API = [1]
    page = 1
    repos = []
    print(name)
    while True:
        response = requests.get(f'https://api.github.com/orgs/{name}/repos?per_page=100&page={page}', auth=auth)
        response_API = response.json()
        for repo in response_API:
            try:
                id = repo['id']
                name = repo['full_name']
                stars = repo['stargazers_count']
                results.put([id,name,stars])
                print(id)
            except TypeError:
                break
        page += 1
        if (response.status_code == 404) or (response_API == []):
            break


def get_names(orgs):
    names = []
    for entry in orgs:
        names.append(entry['login'])
    return names


def get_orgs(pages, auth):
    global last_id
    iteration = 0
    while iteration < pages:
        response_API = requests.get(f'https://api.github.com/organizations'
            f'?since={last_id}&per_page=100', auth=auth).json()
        last_id = response_API[-1]['id']
        iteration += 1
        yield response_API


def create_top(auth):
    global last_id, orgs, repo_names, repo_stars
    for org in get_orgs(2, auth):
        orgs.extend(org)
    names = get_names(orgs)
    #names = ['Jedi-University']

    #queue = Queue()
    #for name in names:
    #    queue.put(name)
    #while queue.empty() is False:
    #    threads = []
    #    for i in range(8):
    #        threads.append(Thread(target = get_repos, args = (queue.get(), auth, results)))
    #        threads[i].start()
    #    for i in range(8):
    #        threads[i].join()

    while results.empty() is False:
        elem = results.get()
        print(elem)
        repo_names[elem[0]] = elem[1]
        repo_stars[elem[0]] = elem[2]
    repo_stars = heapq.nlargest(20, repo_stars.items(), key=lambda i: i[1])

    top_repos = []
    for repo in repo_stars:
        top_repos.append({'id':repo[0], 'org_name':repo_names[repo[0]].split('/')[0], 'repo_name':repo_names[repo[0]].split('/')[1], 'stars_count':repo[1]})

    last_id = 0
    orgs = []
    repo_stars = {}
    repo_names = {}
    return top_repos


last_id = 0
orgs = []
repo_stars = {}
repo_names = {}
results = multiprocessing.Queue()
