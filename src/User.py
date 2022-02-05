from getpass import getpass
from typing import List
import json

from src.crypto import decrypt_text, encrypt_text
from src.data_handle import load_json, update_json, add_confID, USR_DATA



class User:
    def __init__(self, uname, **kwargs) -> None:
        self._username = uname
        if not kwargs:
            self._password = None
            self._id = self.create_id
            self._confessions = []

        else:
            self._password = decrypt_text(kwargs['passw'].encode()) # does it works?
            self._id = kwargs['id']
            self._confessions = kwargs['conf']

    def __str__(self) -> str:
        return f'User object {self._username}'

    @property
    def username(self) -> str:
        return self._username

    @property
    def id(self) -> str:
        return self._id
    
    @property
    def confessions(self) -> List:
        return self._confessions

    @property
    def to_dict(self) -> dict:
        d = {
            "name": self._username,
            "pass": encrypt_text(self._password), # does it works?
            "id": self._id
        }
        return d
    
    @property
    def create_id(self):
        d = load_json(USR_DATA)
        d["id_count"] += 1
        id = d["id_count"]
        add_confID(id) # add id to confessions json file
        update_json(d, USR_DATA) # update user json file
        return id

    @property
    def create_password(self):
        while True:
            pw = getpass()
            if len(pw) >= 4:
                pwc = getpass('Confirm password: ')
                if pw == pwc:
                    self._password = pw # password registered
                    return 
                else:
                    print('error - passwords don\'t match.')
            else:
                print('error - password is too short, minimun of 4 characters is required.')

    def password_check(self, password) -> bool:
        if password == self._password:
            return True
        else:
            return False

    def add_confession(self, conf: str):
        self._confessions.append(conf)

    def del_confession(self, idx):
        self._confessions.pop(idx)


    def add_conf_test(self, conf: List): #FOR TESTING PURPOSES
        for c in conf:
            self._confessions.append(c)
        