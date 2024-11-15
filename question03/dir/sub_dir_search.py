import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            ext = os.path.splitext(full_filename)[-1]
            if ext == '.py':
                print(full_filename)
    except PermissionError:
        pass

search("c:/")