import time

def long_task():
    for i in range(5):
        time.sleep(1)
        print(f"working:{i}\n")

print("Start")

for i in range(5):
    long_task()

print("End")