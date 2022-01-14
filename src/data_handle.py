import json
from typing import Dict, List
from cryptography.fernet import Fernet
from src.User import User

DATA = 'data/data.json'

def load_data() -> Dict:
    """Loads data from encrypted json file, returns a dictionary object"""
    # read key from file and generate Fernet object
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    
    # opening the encrypted file
    with open('data/data.json', 'rb') as enc_file:
        encrypted = enc_file.read()
    
    # decrypting the file
    decrypted = fernet.decrypt(encrypted)
    return decrypted


def save_data(data) -> None:
    """Encrypt and save data to json file. In each run a new key is generated"""
    
    key = Fernet.generate_key()
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

    fernet = Fernet(key)
        
    # encrypting the data  
    encrypted = fernet.encrypt(data)
  
    # Writing data to file 
    with open('data/data.json', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def append_new_user(user: User):
    """append user info to data"""
    user_dict = {
        'name': user.username,
        'password': user.password,
        'confessions': user.confessions 
        }

    data = load_data()

    data['users'].append(user_dict)
    
    save_data(data)

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
    
    d = load_json()

    print(d)
    print(type(d))