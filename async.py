import grequests
from datetime import datetime
import requests


urls = [
    "http://127.0.0.1:5011/orders",
    "http://127.0.0.1:5011/orders/users"
]


def t1():
    s = datetime.now()
    rs = (grequests.get(u) for u in urls)
    x = grequests.map(rs)
    e = datetime.now()

    print("T1")
    print("Elapsed time = ", e-s)

    for r in x:
        print(r.url, r.status_code)


def t2():

    s = datetime.now()
    result = []

    for u in urls:
        r = requests.get(u)
        result.append([u, r.status_code])

    e = datetime.now()

    print("T2")
    print("Elapsed time = ", e - s)

    for x in result:
        print(x)


t1()
t2()