import json

FILE_PATH = "/storage/emulated/0/accounts.json"


def save_data(accounts):
    with open(FILE_PATH, "w") as file:
        json.dump(accounts, file, indent=4)


def load_data():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []