from src.User import User
from src.data_handle import USR_DATA, add_new_user, delete_conf, get_usernames, load_json, add_confID, save_conf, get_confessions


from rich.console import Console

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
    un = input('Username: ')
    # create new user 
    if not user_found(un): 
        console.print(f'{un} is avaliable!', style='bold #eeeeff')
        user = User(un)
        user.create_password
        USERS_CACHE.append(user)
        add_new_user(user)
        # add new user's id to conf.json file

        console.print('Your user was successfully created! You can login now', style='#3afc85')
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

        user = User(username, passw=user_data.get('pass'), id=user_data.get('id'), conf=confessions) 
        return user
    else:
        console.print('error - user not found', style='#fc3d3d')
        return None
        
# UNUSED
# def save_cache():
   # """save cached users to file"""
    # if USERS_CACHE:
        # for user in USERS_CACHE:
            # add_new_user(user)
        # print('Users saved!')


def new_conf(conf: str, author: User):
    """
    Create a new confession
        conf : confession text (str)
        author : user author of the confession (User instance)
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
