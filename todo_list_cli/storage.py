import os
import json

FILE_PATH = 'tasks.json'

def load_data():
    if not os.path.exists(FILE_PATH):
        print(f"{FILE_PATH} file does not exist. Going with an empty list.")
        return []
    try:
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError, json.JSONDecodeError,IOError:
        print("Error loading tasks. Starting with an empty list.")
        return []

def save_data(tasks):
    with open(FILE_PATH, "w") as f:
        json.dump(tasks, f, indent=4)

