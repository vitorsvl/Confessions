import json

from rich.console import Console
from src.data_handle import load_json

# ADICIONANDO CONFESSION
# Já tenho o id do usuário logado
# A confession deve ser salva no arquivo conf.json, na chave do id do usuário que a criou
# Por enquanto as confessions serão salvas sem criptografar
# no arquivo conf.json os ids dos usuários serão as 'chaves' e os 'valores serão no formato de lista
# as listas guardam as cofessions que serão criadas
# Somente o usuário que criou a cofession pode acessá-la
# confessions não podem ser editadas mas podem ser apagadas
 

def new_conf():
    """creates a new confession and save it to json file"""
    pass

def read_conf():
    pass



with open('data/test.json') as jfile:
        data = json.load(jfile)

data['users'][0]['conf'] = {1: "confession1"}
Console().print(data)

 
 # Sets file's current position at offset.
with open('data/test.json', 'r+') as file:
    file.seek(0)
    # convert back to json.
    json.dump(data, file, indent = 4)