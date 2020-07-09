from threading import *
import threading
import time


def sqr(n):
    for x in n:
        x % 2


def cube(n):
    for x in n:
        x % 3


n = [1, 2, 3, 4, 5, 6, 7, 8]
s = time.time()
sqr(n)
cube(n)
e = time.time()
print(e-s)


def sqr(n):
    for x in n:
        print('Remainder after dividing by 2', x % 2)


def cube(n):
    for x in n:
        print('Remainder after dividing by 3', x % 3)


n = [1, 2, 3, 4, 5, 6, 7, 8]
start = time.time()
t1 = Thread(target=sqr, args=(n,))
t2 = Thread(target=cube, args=(n,))
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(end-start)
