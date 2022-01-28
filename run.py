import src.user_func as uf
import src.data_handle as data_handle
from view.screens import clear, confirm, first_screen, display_menu
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

def menu_confessions():
    while True:
        option = display_menu(['New confession', 'My confessions', 'Logout'])
        
        if option == 1:
            # new_confession()
            pass
        elif option == 2:
            # display_confessions()
            pass
        elif option == 3:
            b = confirm('Are you sure?')
            if b:
                clear()
                break
            else:
                clear()


def main(): # where it should be?
    try:
        while True: # main loop

            first_screen() # title até fim do login
            menu_confessions() # menu e prompt, termina quando a opção logout é escolhida 

                # IDEA salvar aqui as confessions no arquivo (salvar também ao ctrl+C)

        
        # TODO handle menu choice (fazer no run mesmo)
        # TODO partir para a criação da parte das confessions em si
        
    except KeyboardInterrupt:
        uf.save_cache()


main()
 # ORGANIZAR E FAZER GIT PUSH 