import json
import os

DATABASE_FILE = "data/database.json"


def load_database():

    if not os.path.exists(DATABASE_FILE):
        return {}

    with open(DATABASE_FILE, "r") as file:
        return json.load(file)


def save_database(database):

    with open(DATABASE_FILE, "w") as file:
        json.dump(database, file, indent=4)
