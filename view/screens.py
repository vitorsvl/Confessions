import sys
import os

ROOT_PATH = os.path.dirname(os.path.abspath("run.py"))
sys.path.insert(0, os.path.dirname(os.path.abspath("run.py")))

from view.colors import RAINBOW_COLORS, SCALES, THEME_COLORS, THEMES, TITLE, ERROR, WARNING, SUCCESS, RAINBOW
from src.User import User
from src.user_func import create_conf, create_user, del_conf, del_user, get_user, new_conf, save_theme, user_found
from src.export import export_confessions, format_datetime, get_dir_path, save_export
# from intro import introduction # the intro

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


### UTILS
console = Console() # global console

def clear():
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')


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

def header(text: str, color: str, align="left") -> None: # TODO change color of horizontal lines 
    highlight = ReprHighlighter()
    console.print()
    console.rule(highlight(text), style=color + ' b', align=align)
    console.print()


def confirm(prompt: Text):
    o = Confirm.ask(prompt)
    return o

### THEME
def define_theme(theme: str):
    """
    Change the value of the theme global variables
    Avaliable themes : seagold, orchid, swamp, autumn, spring, seaborn, oceanic, lgbt 
    """
    global THEME1
    global THEME2
    global COLOR_THEME1
    global COLOR_THEME2

    if theme == 'lgbt':
        THEME1, THEME2 = theme, theme
        COLOR_THEME1 = choice(RAINBOW_COLORS)
        COLOR_THEME2 = choice(RAINBOW_COLORS)

    else:
        THEME1, THEME2 = THEMES[theme].get('theme1'), THEMES[theme].get('theme2')

        COLOR_THEME1 = THEME_COLORS.get(THEME1)
        COLOR_THEME2 = THEME_COLORS.get(THEME2)  


def theme_repr(theme: str) -> Text:
    """Return the name of the theme in rich text as a representation of the theme colors"""
    if theme == 'lgbt':
        lgbt_repr = Text()
        for c, color in zip("lgbtqa+", RAINBOW_COLORS):
            lgbt_repr += Text(c, style=color)
        return lgbt_repr
    else:
        trepr = Text()
        key = 'theme1'
        for c in theme:
            trepr += Text(c, style=THEME_COLORS[THEMES[theme].get(key)])
            key = 'theme2' if key == 'theme1' else 'theme1'
        return trepr


def choose_theme(themes: dict) -> str:
    """
    Show theme options to the user and return the chosen one
    Avaliable themes : seagold, orchid, swamp, autumn, spring, seaborn, oceanic, lgbt
    """
    table = Table( 
        show_header=False,
        show_lines=False,
        box=box.SIMPLE_HEAD,
        show_edge=True,
        padding=(0, 0)
        #row_styles=['dim', 'none']
        )
    table.add_column()
    idx = 1
    th_names = themes.keys()
    names = list(th_names)
    for t in names:
        table.add_row(Text(str(idx) + '.', style='bright_white'), theme_repr(t))
        idx += 1
    
    while True:
        console.print(table)
        p = Prompt.ask("Choose one of the avaliable themes or [cornsilk1 b]C[/cornsilk1 b] to cancel", 
            choices=[str(i) for i in list(range(1, idx))].append('c'), show_choices=True)

        if p.lower() == 'c':
            return
        else:
            try: 
                pos = int(p) - 1
                my_theme = names[pos]
                if confirm(Text("Apply ") + theme_repr(my_theme) + Text(" theme?")):
                    return my_theme
            except (IndexError, ValueError) as _:
                console.print(fancytize("Opção inválida!", type='warning'))
                time.sleep(1)
                clear()

    

### TITLE
def tint(c: str, colors_list: List, bold=False, italic=True) -> Text:
    """
    Color a char or string.
        c: char or str
        colors: list of strings containing colors
    """
    color = choice(colors_list)
    return Text(c, style=Style(color=color, bold=bold, italic=italic))


def display_title(theme: str, theme2=None, char=None, first=False):
    """
    Display the application main title
        theme options : sky, sea, gold, rose, violet or misc 
    """
    
    title = [s.replace('o', char) for s in TITLE] if char else TITLE
    if first:
        console.print('[b i]Welcome to[/b i]')
    # time.sleep(1)
    sty_title = Text()

    if theme == 'lgbt':
        for line, gradient in zip(title, RAINBOW):
            l = Text()
            for c in line:
                l += tint(c, gradient, bold=True, italic=False)
            sty_title = sty_title + l + Text('\n')

    else: #with blend
        n_line = 0
        for line in title:
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
    # time.sleep(2)


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

        menu_str += option + points + Text(str(idx), style='i') + Text('\n')
        idx += 1
        
    menu_str = menu_str[:-1] # removing last \n
    
    # printing the menu
    p = Panel.fit(
            menu_str,
            padding=(1, 3),
            title="[b white]Menu",
            border_style=COLOR_THEME2,
            
        )
    Console().print(p)

    op = Prompt.ask("Choose an option", choices=[str(i) for i in range(1, idx)])  # loop here until avaliable option is chosen
    return int(op)


### USER ###
def login():
    console = Console()
    while True:
        header('👤 Login', COLOR_THEME1)
        console.print("Type your [cornsilk1 i]username[/cornsilk1 i] to login, [cornsilk1 i]N[/cornsilk1 i] to create a new user or [cornsilk1 i]Q[/cornsilk1 i] to quit")
        username = input()
        if username.lower() == "n": # new user
            create_user() # src.user_func

        elif username.lower() == "q": # close application
            if confirm('Are you sure you wanna leave? :\'v'):
                console.print('Come back anytime ^^', style=Style(color=COLOR_THEME1, italic=True))
                time.sleep(1)
                clear()
                exit()

        else: # login
            if user_found(username): # src.user_func
                user = get_user(username) # src.user_func
                console.print(fancytize('User found!', type='success'))
                while True:
                    password = Prompt.ask(f'Password for [b]{user.username}[/b]', password=True)
                    if user.password_check(password): # login success
                        return user 
                    else:
                        console.print(fancytize('Password incorrect', type='error'))
            else:
                console.print(fancytize(f'User {username} not found. Check if username is correct or create a new user', type='warning'))
                time.sleep(1.5)
                clear()

def first_screen():
    # introduction must run only once
    # if os.path.isfile('first_run'): # using a file to do that
        # introduction() # run only if first_run file exists
        # os.remove('first_run')
    define_theme(choice(list(THEMES.keys())[:-1])) # first theme is chosen randomly, lgbt theme is not included in random choice
    display_title(THEME1, theme2=THEME2, first=True, char='*')  
    time.sleep(0.8)
    user = login()
    time.sleep(0.8)
    clear()
    if user.theme: 
        define_theme(user.theme) # set user theme

    display_title(THEME1, THEME2, char='*')
    name_f = fancytize(user.username, color=COLOR_THEME1, bold=True)
    Console().print(Text("Welcome back ") + name_f + Text('!'), style='b')
    time.sleep(0.8)
    return user


################################# CONFESSIONS VIEW ###############################
def new_confession(user: User):
    new_conf_prompts = [
        "What's on your mind?",
        "What do you want to say?",
        "Write down your toughts",
    ]
    console.print(choice(new_conf_prompts) + ' [dim](type [b]C[/b] to cancel, click ENTER when you\'re done)[/dim]', 
        style=Style(color=COLOR_THEME2, italic=True))

    conf = input()
    if conf.lower() != 'c':
        print()
        confirm = Confirm.ask("Save your confession?")
        if confirm:
            confd = create_conf(conf) 
            new_conf(confd, user) 
            console.print(fancytize("Your confession was saved!", type='success'))


def view_confessions(conf: List, index=True, max_len=110):
    """
    Print confessions in rich text
        conf : List containing the confessions
        index : (bool) show indexes, default False
        max_len : max lengh of the confession string, truncate longer strings
    """
    if not conf:
        console.print("You haven't made any confessions yet :v", style='italic')
        time.sleep(1.5)
        return

    header('📜 My Confessions', COLOR_THEME1)
    table = Table( 
        show_header=False,
        show_lines=False,
        box=box.SIMPLE_HEAD,
        show_edge=False,
        padding=(0, 0)
        #row_styles=['dim', 'none']
        )
    if not index:
        table.add_column()
        for c in conf:
            dt = format_datetime(c["time"])
            tex = (c["text"][:max_len] + '.. ') if len(c["text"]) > max_len else c["text"]
            table.add_row(tex, dt)
    else:
        table.add_column()
        table.add_column()

        idx = 1 
        for c in conf:
            dt = format_datetime(c["time"])
            tex = ((c["text"])[:max_len] + '.. ') if len(c["text"]) > max_len else c["text"]
            idxf = Text('    ' + str(idx) + '.', style=Style(color=COLOR_THEME2, bold=True))
            # columns        1   2   3
            table.add_row(idxf, tex, dt)
            idx += 1
    console.print(table)
    print()
    return list(range(1, idx))  #TODO melhorar essa função, criar uma coluna na tabela para as datas


def display_confession(conf: dict):
    clear()
    c = Panel(conf["text"], title=Text(format_datetime(conf["time"])), border_style=COLOR_THEME2, expand=False)
    console.print(c)  
    pr = Prompt.ask("Type [b]d[/b] to [b]delete[/b] or [b]q[/b] to [b]quit[/b]", 
        choices=['D', 'Q', 'd', 'q'], show_choices=False, default='q', show_default=False)
    return pr.lower() # d, q


def menu_confessions(user: User):
    options = [
        Text('💭 New confession'), #1
        Text('📃 My confessions'), #2
        Text('🦄 Change theme'), #3
        Text('📝 Export confessions'), #4 
        Text('💀 Delete user'), #5
        Text('🔘 Logout') #6
        ]
    while True:
        option = display_menu(options)
        if option == 1:
            header('🪶 New confession', COLOR_THEME1)
            new_confession(user)
            time.sleep(2)
            clear()

        elif option == 2: # My confessions
            while True:
                indexes = view_confessions(user.confessions)
                if indexes is None:
                    break

                idx = Prompt.ask("Choose a confession to open or [b i]q[/b i] to exit to previous menu", 
                    choices=[str(i) for i in indexes].append('q'))
                if idx == 'q':
                    break
                else:
                    try:
                        real_idx = int(idx)-1
                        while True:
                            action = display_confession(user.confessions[real_idx]) # action can be D, E or Q (delete, edit, quit)
                            if action == "d":
                                del_conf(user, real_idx)
                                console.print(fancytize("Confession deleted!", type='success'))
                                time.sleep(1.5)
                                break

                            elif action == "q":
                                break
                            
                            else: 
                                console.print(fancytize("Option unavaliable!", type='warning'))

                    except (ValueError, IndexError) as _:
                        console.print(fancytize("Option unavaliable!", type='warning'))  
                        time.sleep(1)            
                clear()    

        elif option == 3: # change theme
            usr_theme = choose_theme(THEMES)
            if usr_theme:
                define_theme(usr_theme)
                console.print(fancytize("Theme changed!", type="success"))
                time.sleep(1.5)
                clear()
                display_title(THEME1, THEME2, char='*')
                time.sleep(2)
                # save theme to json file
                save_theme(usr_theme, user.id)

        elif option == 4: # export
            path = get_dir_path(user=user.username)
            if confirm(Text(f'Your confessions will be exported to "{path}". Procceed?')):
                export_confessions(user.confessions, user.username)
                console.print(fancytize("Confessions exported!", type='success'))
                time.sleep(1.6)
                clear()
        
        elif option == 5: # Delete user
            dl = confirm('Proceed to delete this user and all their confessions? ')
            if dl:
                if del_user(user): # delete exports too ???
                    console.print(fancytize("User was successfully deleted!", type='success'))
            time.sleep(2)
            clear()
            break

        elif option == 6: # logout
            b = confirm('Are you sure?')
            if b:
                clear()
                define_theme(choice(list(THEMES.keys())[:-1])) # reset theme
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