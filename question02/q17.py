import random

person = ['김승현', '김진호', '강춘자', '이예준', '김현주']
work = ['청소', '빨래', '설거지']

a = random.sample(person, 3)

assigned_tasks = dict(zip(a, work))

remaining_person = list(set(person) - set(a))

for person in remaining_person:
    assigned_tasks[person] = "휴식"

# Output the task assignments
print(assigned_tasks)