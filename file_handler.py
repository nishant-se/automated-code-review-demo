import os

def read_file(path):
    with open(path) as f:
        data = f.read()
    return data

def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("File doesn't exist")
