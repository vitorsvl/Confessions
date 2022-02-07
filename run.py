from view.screens import first_screen, menu_confessions


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
# DONE crptografar e esconder senha 
# DONE parte das confessions 
# DONE estrutura de menus
# IDEA usar dois arquivos de dados, o atual para dados dos usuários e outro para as confissões em sí


def main(): # where it should be?
    while True: # main loop

        user = first_screen() # title até fim do login
        menu_confessions(user) # menu e prompt, termina quando a opção logout é escolhida 

# run
main()
### PARTE 3 ### TODO 
# Criar menu para inicial com login, criar user e sair do app ???
# criar funcionalidade para deletar usuário (confessions junto ofc) TODO
# Criar mecanismo de export para as confessions (txt ou markdown ou html?)
