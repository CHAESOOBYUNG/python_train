def read_large_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line.strip()

input_file = 'C:\\Users\\user\\Desktop\\python\\python_plus\\large_file.txt'

for line in read_large_file(input_file):
    print(line)