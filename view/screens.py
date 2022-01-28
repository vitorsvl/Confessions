from rich import console
from view import colors

from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.style import Style
from rich.text import Text
from rich.prompt import Confirm
from rich import box

from random import choice
import time
from sys import path
from os import system, name

THEME = '' # store the color theme for the current run

path.insert(1, 'C:/Users/vitor/Dev/py/project c/src')

from src.user_func import create_user, get_user, user_found


### TITLE
def format_title(text='ConfessionS', scale='rand', patterns=colors.MIRROR, bold=False) -> Text:
    """
    Retuns the string in text in rich format, colored in a color scale pattern of the given color.  
    color variants : sky, sea, gold, rose, violet. Defaults to rand (random)
    """
    # palavra de tamanho 9 (talvez implementar para funcionar qualquer tamanho)
    console = Console()
    
    # choose a random pattern
    if scale == 'rand':
        p = choice(list(patterns.keys()))
        
    else:
        if scale not in patterns.keys():
            console.print(f'error - scale {scale} is not avaliable')        
            return 
        p = scale
    
    # saving chosen theme to global
    global THEME
    THEME = p
    # getting the colors of the chosen pattern 
    colors = patterns.get(p)

    # generate formatted text
    formatted_text = Text()
    for color, char in zip(colors, text):
        f_char = Text(char, style=color)
        formatted_text += f_char
    if bold:
        formatted_text.stylize('bold')

    return formatted_text


def display_header(ftitle, pause=0.1):
    console = Console()
    console.print('[bold]Welcome to[/bold]', end=' ')
    for c in ftitle:
        console.print(c, end='')
        time.sleep(pause)
    print()


# NOTE MENU NOTE #

def display_menu(options):
    """
    param options : List of strings, the options to be displayed in the menu
    """

    g_size = 0
    for option in options:
        g_size = len(option) if len(option) > g_size else g_size

    # generating options string
    idx = 1
    menu_str = ''
    for option in options:
        points = '.........' # TAMANHO FIXO + INDICE = 10 espaços
        if g_size > len(option):
            diff = g_size - len(option)
            points += '.'*diff

        menu_str += option + points + str(idx) + '\n'
        idx += 1
        
    menu_str = menu_str[:-1] # removing last \n
    
    # printing the menu
    p = Panel.fit(
            menu_str,
            padding=(1, 2),
            title="[b white]Menu",
            border_style=colors.THEME_COLORS.get(THEME),
        )
    Console().print(p)

    # prompt
    op = Prompt.ask("Choose an option", choices=[str(i) for i in range(1, idx)])  # loop here until avaliable option is chosen
    return int(op)


def confirm(prompt):
    o = Confirm.ask(prompt)
    return o


def get_input(message, options):
    """Get input from the user 
    message : message to be shown to the user 
    options : avaliable input options (any different input will be disconsidered"""

    while True:
        ip = input(message)
        if ip in options:
            return ip
        else:
            print("error - unavaliable option")


def login():
    console = Console()
    while True:
        console.print('[i]>>>Login[/i]', style='cyan')
        console.print("Enter your username or click [bold]ENTER[/bold] to create a new user")
        username = input()
        if not username:
            create_user() # src.user_func
        else:
            if user_found(username): # src.user_func
                user = get_user(username) # src.user_func
                console.print(fancytize('User found!', type='success'))
                while True:
                    password = Prompt.ask(f'Password for [b]{user.username}[/b]', password=True)
                    if user.password_check(password):
                        return user.username
                    else:
                        console.print(fancytize('Password incorrect', type='error'))
            else:
                console.print(fancytize(f'User {username} not found. Check if username is correct or create a new user', type='warning'))

def clear():
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')


def first_screen():
    title = format_title(bold=True)
    display_header(title, pause=0.05)
    time.sleep(0.8)
    name = login()
    time.sleep(0.8)
    clear()
    name_f = fancytize(name, color=colors.THEME_COLORS.get(THEME), bold=True)
    Console().print(Text("Welcome back ") + name_f + Text('!'), style='b')
    time.sleep(0.8)


def fancytize(text, type=None, bold=False, color=None, blink=None) -> Text:
    """
    type options : error | success | warning
    """
    if type:
        if type == 'error':
            sty = Style(color=colors.ERROR, blink=True, bold=True)
            t = Text(text, style=sty)

        elif type == 'success':
            sty = Style(color=colors.SUCCESS, bold=True, italic=True)
            t = Text(text, style=sty)

        elif type == 'warning':
            sty = Style(color=colors.WARNING)
            t = Text(text, style=sty)
        
        else:
            pass
    else:
        sty = Style(color=color, bold=bold, blink=blink)
        t = Text(text, style=sty)

    return t


if __name__ == '__main__':
        
    first_screen() # 
    
    
    # display_menu(["New confession", "Exit"])


    Console().print(Panel('menu', title='a panel', width=12))

    
    # TODO Olhar o módlulo prompt da rich (exemplos)
    # TODO solve the path/import issue BUG 
