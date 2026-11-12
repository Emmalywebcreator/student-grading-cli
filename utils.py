import time
from functools import wraps


def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            end_time = time.perf_counter()
            elapsed = end_time - start_time
            print(f"{func.__name__} took {elapsed:.4f}s")

    return wrapper
