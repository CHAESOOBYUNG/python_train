import time

def elapsed(original_func):
    def wrapper():
        start = time.time()
        result = original_func()
        end = time.time()
        