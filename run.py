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
    try:
        while True: # main loop

            user = first_screen() # title até fim do login
            menu_confessions(user) # menu e prompt, termina quando a opção logout é escolhida 
    except KeyboardInterrupt:
        print('You chose to leave..')
# run
main()
### PARTE 3 ### TODO 
# ??? Criar menu para inicial com login, criar user e sair do app ???

# TODO criar funcionalidade para deletar usuário (confessions junto ofc) 

# TODO Criar mecanismo de export para as confessions (txt ou markdown ou html?)

# TODO salvar a data em que a confession foi feita
    # TODO
    # Confessions agora são dicionarios, com o texto na chave conf e a data na chave time
    # printar a data das confessions junto ao texto nas funções de mostrar confessions NOTE falta arrumar em view_confessions

    # DONE Mudar o formato de conf.json ?? fazer cada id de usuário ter uma lista, 
    # DONE dentro da lista objetos confession, com atributos conf e time
    # DONE converter o objeto datetime em uma string com melhor vizualização da data e hora, criar uma função pra isso
    # DONE continuar trabalhando no modulo de export (que por enquanto se chama test e tá no lugar errado)
    # VC É INCRÍVEL POR FAZER ISSO (e tantas outras coisas)
    
# DONE opção de escolher o tema no meu do usuário (menu confessions)

# DONE colocar também a opção exit para fechar a aplicação

# DONE guardar o tema escolhido pelo usuário e ativá-lo toda vez que ele fizer login
    # salvar no user_data json junto com as informações do usuário, salvar também na classe

# DONE implementar parte de escolher o tema 
# resetar tema ao logout

# DONE ao login, se o user tiver um tema salvo no json, aplica-lo


# TODO FINALIZANDO TODO
# O diretório confessions data deve ser criado na primeira utilização