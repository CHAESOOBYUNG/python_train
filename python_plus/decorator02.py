import time

def elapsed(original_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs) # 기존 함수 수행
        end = time.time()
        print(f"함수 수행 시간:{end - start}")
        return result
    return wrapper

@elapsed
def myfunc(msg):
    """데코레이터 확인 함수"""
    print(f"{msg}를 출력합니다.")

myfunc("You need python")
