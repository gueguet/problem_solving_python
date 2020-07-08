# https://www.youtube.com/watch?v=Up4StKwusdo

import threading
import time
from threading import *

"""
# crash course multythreading in python :
# python mutltithreading without class

print(current_thread().getName())

def mt():
    print("Child Thread")


child = Thread() # by default, nothing will be called --> but we can specify a target
child.start()
print("Executing thread name :", current_thread().getName())


# python multithreading by extending Thread class
class mythread(Thread):
    def run(self):
        for x in range(2):
            print("Hi from child")
            print(current_thread().getName())


a = mythread() # create only one other thread !
a.start()

b = mythread() # second other thread (3 in total)
b.start()

a.join()
b.join()


print("Bye from", current_thread().getName())


# example of use to increase rapidity of code execution :
def sqr(n):
    for x in n:
        time.sleep(1)
        print('Remainder after dividing by 2', x % 2)


def cube(n):
    for x in n:
        time.sleep(1)
        print('Remainder after dividing by 3', x % 3)


n = [1, 2, 3, 4, 5, 6, 7, 8]
start = time.time()
t1 = Thread(target=sqr, args=(n,))
t2 = Thread(target=cube, args=(n,))
t1.start()
time.sleep(1)
t2.start()
t1.join()
t2.join()
end = time.time()
print(end-start)
"""


### BACK TO EXERCISE 


test_array = [1, 5, 2, 3]
res_array = []


def just_sleep(num):
    time.sleep(num)
    res_array.append(num)
    print("{} has been append to res list.".format(num))


if __name__ == "__main__":
    for num in test_array:
        new_thread = Thread(target=just_sleep, args=(num,))
        new_thread.start()
        # new_thread.join() --> don't want that otherwise it the program will wait until the end of each thread to launch the other one !
    

    # need a condition toherwise it will directly return the results without the threads beeing executed 
    while(len(res_array) != len(test_array)):
        pass

    print("Sorted array : ", res_array)


