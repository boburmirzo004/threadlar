import threading
import time
import random

# 1-masala
def show_thread_name():
    time.sleep(1)
    print("Thread name:",{threading.current_thread().name})

t1=threading.Thread(target=show_thread_name)
t1.start()




# 2-masala
def show_start_time():
    start_time = time.time()
    print("Thread name:",threading.current_thread().name, "Start time:",start_time)

threads = []

for i in range(4):
    t = threading.Thread(target=show_start_time)
    t.start()
    threads.append(t)




# 3-masala

def show_thread_name():
    sleep_time = random.randint(1,5)
    time.sleep(sleep_time)
    print("Thread name:", threading.current_thread().name, "Sleep time:", sleep_time)

threads = []
for i in range(5):
    t = threading.Thread(target=show_thread_name)
    threads.append(t)
    t.start()




# 4-masala

natija = []
def square_number(a):
    kvadrat = a**2
    natija.append(kvadrat)
    print("Thread name:",threading.current_thread().name, "Kvadrat:", kvadrat)

threads = []

for i in range(5):
    t = threading.Thread(target=square_number, args=(i,))
    threads.append(t)
    t.start()