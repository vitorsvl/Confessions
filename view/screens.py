import sys
import os

ROOT_PATH = os.path.dirname(os.path.abspath("run.py"))
sys.path.insert(0, os.path.dirname(os.path.abspath("run.py")))

from view.colors import SCALES, THEME_COLORS, TITLE, ERROR, WARNING, SUCCESS
from src.User import User
from src.user_func import create_user, del_conf, get_user, new_conf, user_found

from rich import console
from rich import box
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.style import Style
from rich.text import Text
from rich.prompt import Confirm
from rich.highlighter import ReprHighlighter

from typing import List
from random import choice
from os import system, name
import time


def define_blend(theme) -> str:
    """Define the blend for the current run, the two color scales that will appear on the title, gets theme color and returns theme2 color"""
    d = {}
    d['sky'] = choice(['sea', 'violet', 'sky']) 
    d['sea'] = choice(['rose', 'sky', 'sea'])
    d['rose'] = choice(['gold', 'violet', 'rose'])
    d['gold'] = choice(['rose', 'gold'])
    d['violet'] = choice(['rose', 'sky', 'violet'])
    return d[theme]
# randomly choose the color theme for the current run
# the choice might be overwitten in format_title function with the scale param
THEME = choice(list(THEME_COLORS.keys()))
THEME2 = define_blend(THEME) 
COLOR_THEME = THEME_COLORS.get(THEME)
COLOR_THEME2 = THEME_COLORS.get(THEME2)
console = Console()


### TITLE
def tint(c: str, colors_list: List, bold=False, italic=False) -> Text:
    """
    Color a char or string.
        c: char or str
        colors: list of strings containing colors
    """
    color = choice(colors_list)
    return Text(c, style=Style(color=color, bold=bold, italic=italic))


def display_title(theme: str, blend=False, theme2=None):
    """
    Display the application main title
        theme options : sky, sea, gold, rose, violet or misc 
    """
    console.print('[b i]Welcome to[/b i]')
    time.sleep(1)
    sty_title = Text()
    if not blend and not theme2: # no blend
        for line in TITLE:
            l = Text()
            for c in line:
                l += tint(c, SCALES[theme], bold=True)
            sty_title = sty_title + l + Text('\n')
        sty_title = sty_title[:-1] 

    else: #with blend
        n_line = 0
        for line in TITLE:
            l = Text()
            if n_line < 3:
                for c in line:
                    l += tint(c, SCALES[theme])
            elif n_line == 3:
                for c in line:
                    l += tint(c, SCALES[theme] + SCALES[theme2])
            else:
                for c in line:
                    l += tint(c, SCALES[theme2])
            sty_title = sty_title + l + Text('\n')
            n_line += 1
        sty_title = sty_title[:-1] 
    Console().print(sty_title)
    time.sleep(2)


# NOTE MENU NOTE #

def display_menu(options):
    """
    param options : List of Text objects, the options to be displayed in the menu
    """

    g_size = 0
    for option in options:
        g_size = len(option) if len(option) > g_size else g_size

    # generating options string
    idx = 1
    menu_str = Text()
    for option in options:
        points = Text('.........') # TAMANHO FIXO + INDICE = 10 espaços
        if g_size > len(option):
            diff = g_size - len(option)
            points += Text('.'*diff)

        menu_str += option + points + Text(str(idx)) + Text('\n')
        idx += 1
        
    menu_str = menu_str[:-1] # removing last \n
    
    # printing the menu
    p = Panel.fit(
            menu_str,
            padding=(1, 2),
            title="[b white]Menu",
            border_style=COLOR_THEME2,

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


def clear():
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

### USER ###

def login():
    console = Console()
    while True:
        header('👤 Login', COLOR_THEME)
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
                        return user
                    else:
                        console.print(fancytize('Password incorrect', type='error'))
            else:
                console.print(fancytize(f'User {username} not found. Check if username is correct or create a new user', type='warning'))


def first_screen():

    display_title(THEME, blend=True, theme2=THEME2)  # Blend?
    time.sleep(0.8)
    user = login()
    time.sleep(0.8)
    clear()
    name_f = fancytize(user.username, color=COLOR_THEME2, bold=True)
    Console().print(Text("Welcome back ") + name_f + Text('!'), style='b')
    time.sleep(0.8)
    return user


def fancytize(text, type=None, bold=False, color=None, blink=None) -> Text:
    """
    type options : error | success | warning
    """
    if type:
        if type == 'error':
            sty = Style(color=ERROR, blink=True, bold=True)
            t = Text(text, style=sty)

        elif type == 'success':
            sty = Style(color=SUCCESS, bold=True, italic=True)
            t = Text(text, style=sty)

        elif type == 'warning':
            sty = Style(color=WARNING)
            t = Text(text, style=sty)
        
        else:
            pass
    else:
        sty = Style(color=color, bold=bold, blink=blink)
        t = Text(text, style=sty)

    return t


################################# CONFESSIONS VIEW ###############################
def new_confession(user: User):
    new_conf_prompts = [
        "What's on your mind?",
        "What do you want to say?",
        "Write down your toughts",
    ]
    console.print(choice(new_conf_prompts) + '(click ENTER when you\'re done)', 
        style=Style(color=COLOR_THEME2, italic=True))

    conf = input()
    confirm = Confirm.ask("Save your confession?")
    if confirm:
        new_conf(conf, user)
        console.print(fancytize("Your confession was saved!", type='success'))


def  view_confessions(conf: List, index=True, max_len=80):
    """
    Print confessions in rich text
        conf : List containing the confessions
        index : (bool) show indexes, default False
        max_len : max lengh of the confession string, truncate longer strings
    """
    if not conf:
        console.print("You haven't made any confessions yet :v", style='italic')
        time.sleep(2)
        return

    header('📜 My Confessions', COLOR_THEME)
    # hline = '----------'
    table = Table( 
        #title=hline + 'My Confessions' + hline,
        #title_style=Style(color=COLOR_THEME, bold=True, italic=True), # TODO Dar um jeito de colocar as linhas horizontais
        show_header=False,
        show_lines=False,
        box=box.SIMPLE_HEAD,
        show_edge=False,
        border_style=Style(bold=True, dim=False, color='green'),
        padding=(0, 0)
        #row_styles=['dim', 'none']
        )
    if not index:
        for c in conf:
            tex = (c[:max_len] + '..') if len(c) > max_len else c
            table.add_row(tex)
    else:
        table.add_column()
        idx = 1 
        for c in conf:
            tex = (c[:max_len] + '...') if len(c) > max_len else c
            table.add_row(Text('    ' + str(idx) + '.', style=Style(color=COLOR_THEME2, bold=True)), tex)

            idx += 1
    console.print(table)
    print()
    return list(range(1, idx))


def header(text: str, color: str, align="left") -> None: # TODO change color of horizontal lines 
    highlight = ReprHighlighter()
    console.print()
    console.rule(highlight(text), style=color, align=align)
    console.print()


def display_confession(conf):
    c = Panel(conf, border_style=COLOR_THEME2, expand=False)
    console.print(c)  
    pr = Prompt.ask("Type [b]d[/b] to [b]delete[/b] or [b]q[/b] to [b]quit[/b]", 
        choices=['D', 'Q', 'd', 'q'], show_choices=False, default='q', show_default=False)
    return pr.lower() # d, q ou e


def menu_confessions(user: User):
    while True:
        option = display_menu([Text('💭 New confession'), Text('📃 My confessions'), Text('⚪ Logout')])
        
        if option == 1:
            header('🪶 New confession', COLOR_THEME)
            new_confession(user)
            time.sleep(2)
            clear()

        elif option == 2:
            while True:
                indexes = view_confessions(user.confessions)
                if indexes is None:
                    break

                idx = Prompt.ask("Choose a confession to open or [b i]q[/b i] to exit to previous menu", 
                    choices=[str(i) for i in indexes].append('q'))
                if idx == 'q':
                    break
                else:
                    real_idx = int(idx)-1
                    action = display_confession(user.confessions[real_idx]) # action can be D, E or Q (delete, edit, quit)

                    # except IndexError:
                    #     console.print(fancytize("Option unavaliable!", type='warning'))

                    if action == "d":
                        del_conf(user, real_idx)
                        console.print(fancytize("Confession deleted!", type='success'))
                        time.sleep(1.5)

                    elif action == "q":
                        pass
            clear()    

        elif option == 3:
            b = confirm('Are you sure?')
            if b:
                clear()
                break
            else:
                clear()


if __name__ == '__main__':
    
    # first_screen() 
    c = ['I wanna be rich', 
        'but i feel guilty',
        'o o o my god',
        'what\'s happening to me, walking down Montana o o o same old dull routines same alo gobi walking down montana o o o']
    #view_confessions(c, index=True, max_len=200)
    #display_confession('THis is a confession for testing purposes')
    while True:
        user = login()
        print(user.confessions)

        #user.add_conf_test(c)
        menu_confessions(user)


# NOTE IDEA Fazer os itens de exibição aparecerem centralizados 
# e os itens de input justificado para esquerda
#  
