from genericpath import exists
import os
import datetime

import schemas

STORAGE = os.path.join(os.path.dirname(__file__), "storage")
INPUT = os.path.join(STORAGE, "input")
OUTPUT = os.path.join(STORAGE, "output")

for path in [STORAGE, INPUT, OUTPUT]:
    os.makedirs(path, exist_ok=True)

def save_text(data, path: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(data)

def load_text(path: str):
    if not os.path.exists(path):
        raise ValueError
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    return data

def save_input(data: schemas.Input):
    filename = "text" + datetime.datetime.now().strftime("%m%d%H%M") + ".txt"
    path = os.path.join(INPUT, filename)
    save_text(data, path)
    return filename

def load_input(filename: str):
    path = os.path.join(INPUT, filename)
    if not os.path.exists(path):
        raise ValueError
    data = load_text(path)
    return data

def save_output(data: schemas.Output, filename: str):
    path = os.path.join(OUTPUT, filename)
    save_text(data, path)

def load_output(filename: str):
    path = os.path.join(OUTPUT, filename)
    return load_text(path)

def check_output(filename: str):
    path = os.path.join(OUTPUT, filename)
    return os.path.exists(path)
