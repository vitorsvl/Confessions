import src.user_func as uf
import src.data_handle as data_handle
# from src.User import User 
'''
Confessions (nome provisório)

A ideia primária é fazer uma aplicação que permita ao usuário escrever textos (confissões).

Funcionalidades iniciais
- Sistema de usuários: Criação de usuário e login com usuário existente (username e senha)
- Permitir a criação de confissões por usuários cadastrados
- Salvar confissão associando-a ao usuário que a criou
- Menu de navegação
'''
# DONE parte de manipulação de usuários
# TODO crptografar e esconder senha 
#from getpass import getpass
#password = getpass()
# TODO parte das confessions 
# TODO estrutura de menus
# IDEA usar dois arquivos de dados, o atual para dados dos usuários e outro para as confissões em sí


def main(): # where it should be?
    try:
        uf.login()
    except KeyboardInterrupt:
        uf.save_cache()


main()