"""
Note : In a program run it stores all memory, but in one time  program run only

"""


import functools 
import time

@functools.lru_cache(maxsize= None)
def fx(n):
    time.sleep(5)
    return n*5


print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

print(fx.cache_info()) #CacheInfo(hits=0, misses=3, maxsize=None, currsize=3)

print(fx(20))
print("done for 28")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")
print(fx.cache_info()) #CacheInfo(hits=3, misses=3, maxsize=None, currsize=3)

"""Note what will hapen inn above program in first time it will take a long time but in second time it will take very fadt because it fetch it from  cache It is memoize NOT memorize

So Memoization ensures that method does not execute more than once for same inputs by storing the results in the data structure

Memoization is a technique used in computer programming to reduce the execution time of programs.

Memoization is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again

To memoize a function in Python, we can use a utility supplied in Python’s standard library—the functools.lru_cache decorator.

lru_cache isn’t hard to use. The above example would be memoized with lru_cache like this:

from functools import lru_cache
from math import sin

@lru_cache
def sin_half(x):
    return sin(x)/2
Now, every time you run the decorated function, lru_cache will check for a cached result for the inputs provided. If the result is in the cache, lru_cache will return it


"""



"""@lru_cache(360)
def sin_half(x):
    return sin(x)/2
    
    
This caches a maximum of 360 possible values for x, and their corresponding responses.


If you want to examine the statistics for a given function cache, use the .cache_info() method on the decorated function (e.g., sin_half.cache_info())"""

"""
When to use lru_cache
like you know limited value 
like you know when repeated value

When not to use lru_cache 
you know every time unique value
when you using continus loop funiction calling  in that no will repeat

"""



