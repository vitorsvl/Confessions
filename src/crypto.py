import json
from winreg import LoadKey
from cryptography.fernet import Fernet



def load_data():
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


################
# NOTE: generate_key should be called in the first run, afterwards call load_key instead 

def generate_key() -> Fernet:
    """Generates a key and a Fernet object to encrypt and decrypt text based on the key.
    The key is also stored in a .key file"""
    # generating key
    key = Fernet.generate_key()
    # writing key to file
    with open('src/passkey.key', 'wb') as filekey:
        filekey.write(key)
    # generating Fernet object with the key
    f = Fernet(key)
    return f


def load_key() -> Fernet:
    """Read a key from the .key file and returns the associated Fernet object"""
    with open('src/passkey.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    return fernet


def encrypt_text(text) -> bytes:
    """Returns the encrypted bytes for the passed text using Fernet"""
    # generate fernet object
    try:
        fernet = load_key()
        print('used load_key')
    except FileNotFoundError:
        fernet = generate_key()
        print('used generate_key')

    encrypted = fernet.encrypt(text.encode()) # string must be converted to bytes
    return encrypted.decode() # decode bytes to string (neeaded to write to json)


def decrypt_text(enc) -> str:
    """Returns the corresponded text for the passed encrypted text"""
    fernet = load_key()
    return fernet.decrypt(enc).decode() # bytes string is decoded to regular string


if __name__ == '__main__':
    # TESTS
    #fobj = generate_key()
    with open('data/test.json') as jfile:
        data = json.load(jfile)
    po = data['users'][1].get('pass') # get password
    p = po.encode()
    print(p)
    print(type(p))

    fernet = load_key()
    enc = fernet.encrypt(p)
    print(enc)
    print(type(enc))

    with open('test.txt', 'wb') as t:
        t.write(enc)

    with open('test.txt', 'rb') as t:
        cryp = t.read()

    print(cryp)
    pd = fernet.decrypt(cryp)
    print(pd)
    pd = pd.decode()

    print('--------------------------')
    print(pd == po)


