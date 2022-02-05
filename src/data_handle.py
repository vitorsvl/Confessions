import json
from typing import Dict, List
import sys
import os


ROOT_PATH = os.path.dirname(os.path.abspath("run.py"))
sys.path.insert(0, os.path.dirname(os.path.abspath("run.py")))

# from src.User import User


#### json functions ###

def load_json(path) -> Dict:
    """Loads data from a json file and returns it in a dictionary"""
    with open(path) as jfile:
        data = json.load(jfile)
    return data


def update_json(json_data: dict, json_file: str):
    """Updates json file.
            json_data : dictionary representing the updated data
            json_file : path to json file 
    """
    # Sets file's current position at offset.
    with open(json_file, 'r+') as file:
        file.seek(0)
        # convert back to json.
        json.dump(json_data, file, indent = 4)


#### User functions ####
USR_DATA = 'data/user_data.json'

def add_new_user(user):
    """Add new user's data to the json data file"""
    data = load_json(USR_DATA)

    # appending user's data to json data
    data["users"].append(user.to_dict)
    # Sets file's current position at offset.
    update_json(data, USR_DATA)


def get_usernames() -> List:
    """Returns a list of the usernames of all users registered in the database"""
    data = load_json(USR_DATA)
    usernames = [d.get("name") for d in data["users"]]
    return usernames


#### Confessions functions ####
CONF_DATA = 'data/conf.json'

def add_confID(id):
     
    data = load_json(CONF_DATA)
    data[id] = []

    update_json(data, CONF_DATA)


def save_conf(conf: str, user_id):

    data = load_json(CONF_DATA)
    
    try:
        data[user_id].append(conf)
    except KeyError:
        try:
            data[str(user_id)].append(conf)
        except KeyError:
            print('error - user not found')
            return
    update_json(data, CONF_DATA)
    

def delete_conf(conf_id, user_id):
    """delete confession from json file"""
    data = load_json(CONF_DATA)
    try:
        del data[str(user_id)][conf_id]
    except KeyError:
        try:
            del data[user_id][conf_id]
        except KeyError:
            print('error - user not found')
            return
    print(data)
    # update_json(data, CONF_DATA)
    open(CONF_DATA, "w").write(
    json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
)


def get_confessions(user_id) -> List:
    """get the confessions list by the associated user id"""
    data = load_json(CONF_DATA)
 
    try: 
        conf = data[user_id]
    except KeyError:
        try:
            conf = data[str(user_id)]
        except KeyError:
            print('error - user not found')
            return

        return conf

         
if __name__ == '__main__':

    # save_conf("my first confession", '124')
    con = get_confessions('124')
    for c in con:
        print(c)

    save_conf('aaaaaaaaa', '125')
    print(get_confessions('125'))

    




