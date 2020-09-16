from time import time
def timer(func):
    def timed_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        return result, t2 - t1
    return timed_func