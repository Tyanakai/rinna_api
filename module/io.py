import os
import datetime
import string

#import schemas

storage_path = os.path.dirname(__file__)
lower_case = string.ascii_lowercase

def save_txt(data, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(data)

def load_txt(path: str):
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    return data

def save_input(data):

    filename = "text" + datetime.datetime.now().strftime("%m%d%H%M") + ".txt"
    path = os.path.join(storage_path, "input", filename)
    save_txt(data, path)
    return filename

def load_input(filename):
    path = os.path.join(storage_path, "input", filename)
    data = load_txt(path)
    return data

def save_output(data, filename):
    path = os.path.join(storage_path, "output", filename)
    save_txt(data, path)

def load_output(filename):
    path = os.path.join(storage_path, "output", filename)
    return load_txt(path)

def check_output(filename):
    path = os.path.join(storage_path, "output", filename)
    return os.path.exists(path)
