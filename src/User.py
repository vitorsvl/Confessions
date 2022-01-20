from getpass import getpass
from src.crypto import decrypt_text, encrypt_text


class User:
    def __init__(self, uname, **kwargs) -> None:
        self._username = uname
        if not kwargs:
            self._password = None
            self._confessions = []
        else:
            self._password = decrypt_text(kwargs['passw'].encode()) # does it works?
            self._confessions = kwargs['conf']


    @property
    def username(self) -> str:
        return self._username

    @property
    def confessions(self) -> str:
        return self._confessions

    @property
    def to_dict(self) -> dict:
        d = {
            "name": self._username,
            "pass": encrypt_text(self._password), # does it works?
            "conf": self._confessions
        }
        return d

    def create_password(self):
        while True:
            pw = getpass()
            if len(pw) >= 4:
                pwc = getpass('Confirm password: ')
                if pw == pwc:
                    print('Success!')
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

