""" 
When you  want to Resources parrallely download
one thread can started only max one time

Note you must thinking  why instead of using multithreading supply all power to one thread and run it efficently and fast BUT  like there is server speed and network speed, server speed is like speed at which server gives you and network speed at which you downloading it but even you increasen network speed it will download at max  upto server speed So Use multithreading instead"""

import threading
import time
from concurrent.futures import Executor, ThreadPoolExecutor

def func(seconds):
    print ( f"Sleeping for {seconds} seconds ")
    time.sleep(seconds)

time1 = time.perf_counter()
func(4)
func(2)
func(1)

time2 = time.perf_counter()

print(time2-time1) # 7.018140299998777

t1 = threading.Thread(target= func , args= [4])
t2 = threading.Thread(target= func , args= [2])
t3 = threading.Thread(target= func , args= [1])


t1.start() # what it does it start thread 1 immediately and running in background
t2.start()
t3.start()


time1 = time.perf_counter()
print(time1-time2) #0.0032211000016104663

t4 = threading.Thread(target= func , args= [4])
t5 = threading.Thread(target= func , args= [2])
t6 = threading.Thread(target= func , args= [1])

t4.start() 
t5.start()
t6.start()

t4.join() # it will wait for task 1 to complete
t5.join()
t6.join()

# note in this t5 and t6 already completed becuase they took less time and started parrleley

time2 = time.perf_counter()
print(time2-time1) #4.0033925000007



def poolingdemo():
    with ThreadPoolExecutor() as Executor:
        future1 = Executor.submit(func , 3)
        