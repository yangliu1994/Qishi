
import functools
import time
import sys
# from IPython.display import Image

def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args,**kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

def cache(func):
    """Keep a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache

def fib(n):
    if n <= 1:
        return n
    a = 0
    b = 1
    while n > 1:
        c = a + b
        a = b
        b = c
        n -= 1
    return b

print(fib(100))

