from getpass import getpass
from src.User import User
from src.data_handle import add_new_user, get_usernames, load_json



# TODO Descobrir como funciona json. Objetivo: Criar um arquivo json para
# salvar os dados dos usuários. Talvez o username em cada 'chave' e vinculadas
# a cada um colocar as outras informações.
# Descobrir uma maneira de criptografar a senha no json (será???)
# Descobrir uma maneira de instanciar classes python a partir de dados de um json

USERS_CACHE = []

# Criar um 'cache' que guarda os usuários instanciados na execução atual
# Ao chamar a get_user, buscar o usuário primeiro na cache
# A cache seria uma lista de instâncias da classe User
# Se o usuário buscado não estiver na cache criar uma nova instância com os
# dados que estarão no arquivo data

def user_found(username) -> bool:
    return username in get_usernames()


def create_user():
    un = input('Username: ')
    # create new user 
    if not user_found(un): 
        print(f'{un} is avaliable!')
        user = User(un)
        user.create_password()
    
        add_new_user(user) # IDEA salvar informação no arquivo apenas no final da execução,
        # assim modificações durante a execução não envolvem manipulação de arquivo
        USERS_CACHE.append(user)
        print('Your user was successfully created! You can login now')
    else:
        print('Username already taken. Please enter a different one')


def get_user(username) -> User:
    """Returns the User object of the given username"""
    # look in cache
    if USERS_CACHE:
        for user in USERS_CACHE:
            if user.username == username:
                return user
    # look in file
    data = load_json()
    if user_found(username):

        for d in data['users']:
            if d.get('name') == username:
                user_data = d
                break   

        user = User(username, passw=user_data.get('pass'), conf=user_data.get('conf'))
        return user
    else:
        print('error - user not found')
        

def login():
    print('Welcome to Confessions!')
    while True:
        print("Enter your username or click ENTER to create a new user")
        username = input()
        if not username:
            create_user() 
        else:
            if user_found(username):
                user = get_user(username)
                print('User found!')
                while True:
                    password = getpass(f'Password for {user.username}: ')
                    if user.password_check(password):
                        print('logged in!')
                        break
                    else:
                        print('wrong password!')

            else:
                print(f'User {username} not found. Check if username is correct or create a new user')

