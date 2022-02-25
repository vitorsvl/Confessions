from src.data_handle import USR_DATA, add_new_user, delete_conf, delete_user, get_usernames, load_json, save_theme_json, save_conf, get_confessions
from src.User import User

from rich.console import Console
from rich.prompt import Prompt

from datetime import datetime
from typing import Dict

# DONE Descobrir como funciona json. Objetivo: Criar um arquivo json para
# salvar os dados dos usuários. Talvez o username em cada 'chave' e vinculadas
# a cada um colocar as outras informações.
# Descobrir uma maneira de criptografar a senha no json (será???)
# Descobrir uma maneira de instanciar classes python a partir de dados de um json

#### NOTE USER FUNCTIONS ####
USERS_CACHE = []
console = Console()
# DONE Criar um 'cache' que guarda os usuários instanciados na execução atual
# Ao chamar a get_user, buscar o usuário primeiro na cache
# A cache seria uma lista de instâncias da classe User
# Se o usuário buscado não estiver na cache criar uma nova instância com os
# dados que estarão no arquivo data

def user_found(username) -> bool:
    # check cache first
    if username in [u.username for u in USERS_CACHE]:
        return True
    
    return username in get_usernames()


def create_user():
    while True:
        un = input('Username: ')
        # create new user 
        if len(un) < 3:
            console.print('Usename must have at least 3 characters', style='#fc3d3d')
        else:
            if not user_found(un): 
                console.print(f'{un} is avaliable!', style='bold #eeeeff')
                user = User(un)
                user.create_password
                USERS_CACHE.append(user)
                add_new_user(user)

                console.print('Your user was successfully created! You can login now', style='#3afc85')
                return
            else:
                console.print('Username already taken. Please enter a different one', style='#fc3d3d')


def get_user(username) -> User:
    """Returns the User object of the given username"""
    # look in cache
    if USERS_CACHE:
        for user in USERS_CACHE:
            if user.username == username:
                return user
    # look in file
    data = load_json(USR_DATA)
    if user_found(username):

        for d in data['users']:
            if d.get('name') == username:
                user_data = d
                break   
        # getting the confessions
        confessions = get_confessions(user_data["id"])

        user = User(username, passw=user_data.get('pass'), id=user_data.get('id'), conf=confessions, theme=user_data.get('theme')) 
        return user
    else:
        console.print('error - user not found', style='#fc3d3d')
        return None


def del_user(user: User) -> bool:
    while True:
        password = Prompt.ask(f'Password for [b]{user.username}[/b]', password=True)
        if user.password_check(password): # login success
            delete_user(user) # deleting user's data from json files 
            del user # deleting user object
            return True
        else:
            console.print('Password incorrect', style='#fc3d3d')   
# UNUSED
# def save_cache():
   # """save cached users to file"""
    # if USERS_CACHE:
        # for user in USERS_CACHE:
            # add_new_user(user)
        # print('Users saved!')
def create_conf(text: str) -> dict:
    """Creates a confession with the given text and returns in dict format with text and datetime"""
    d = dict.fromkeys(["text", "time"])
    d["text"] = text
    d["time"] = datetime.now().isoformat()
    return d


def new_conf(conf: Dict, author: User): 
    """
    Create a new confession
        conf : dict representing the confession (text + datetime)
        author : user author of the confession (User object)
    """
    # saving to class
    author.add_confession(conf)
    # saving to file
    save_conf(conf, author.id)


def del_conf(user: User, conf_idx):
    """
    Delete a confession
    """
    # del from class
    user.del_confession(conf_idx)
    # del from file
    delete_conf(conf_idx, user.id)


def save_theme(theme: str, user_id):
    """Save user theme preference"""
    save_theme_json(theme, user_id)
    
    