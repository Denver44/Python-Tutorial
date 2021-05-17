# --------------function caching for optimization---------------

import time
from functools import lru_cache  # function caching for optimization


@lru_cache(maxsize=3) # in maxsize we have to write how much value you want to cache.
def some_work(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("Now running some work")
    print(some_work(3))
    print(some_work(10))
    print(some_work(6))
    print(some_work(2))
    print("Done... Calling again")
    input("Enter something user : ")
    print(some_work(10))
    print("Called again")
