import time

def elapsed(original_func):
    def wrapper():
        start = time.time()
        result = original_func()
        end = time.time()
        print(f"함수 수행 시간:{end - start}")
        return result
    return wrapper

@elapsed
def myfunc():
    print("함수가 실행됩니다.")

myfunc()