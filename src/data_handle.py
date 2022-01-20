import json
from typing import Dict, List
from src.User import User

DATA = 'data/data.json'

#### FUNCTIONS ABOVE ARE UNUSED AT THE MOMENT

def load_json() -> Dict:
    """Loads data from a json file and returns it in a dictionary"""
    with open(DATA) as jfile:
        data = json.load(jfile)
    return data


def add_new_user(user: User):
    """Add new user's data to the json data file"""
    data_json = load_json()

    # appending user's data to json data
    data_json["users"].append(user.to_dict)
    # Sets file's current position at offset.
    with open(DATA, 'r+') as file:
        file.seek(0)
        # convert back to json.
        json.dump(data_json, file, indent = 4)


def get_usernames() -> List:
    """Returns a list of the usernames of all users registered in the database"""
    data = load_json()
    usernames = [d.get("name") for d in data["users"]]
    return usernames


if __name__ == '__main__':
    pass