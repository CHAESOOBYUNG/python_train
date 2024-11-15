import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print(f"working:{i}")

print("Start") # (1개 쓰레드)

threads=[]

for i in range(5):
    t = threading.Thread(target=long_task) # 쓰레드 생성
    threads.append(t)

for t in threads:
    t.start() # 쓰레드 실행 (5개 쓰레드)

print("End")