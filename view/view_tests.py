from turtle import width
from typing import List
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
from rich.align import Align
from rich.panel import Panel
from rich.style import Style
from rich.text import Text
from random import choice
import time
from sys import path

'''
menu = Panel("1.........faz isso\n2........faz aquilo\n3..........sair", 
    title="MENU",
    width=35, 
    border_style=Style(bold=True, color="#00ff88"), 
    style=Style(bold=True, color="white", encircle=True)
    )

Console().print(menu)
'''
options = ['as', 'aaa', 'aa', 'sdfsddgg', 'zzzzzzzzzzzzzzz']
# getting the size of the bigger option (len), it will be use as reference to print aligned
'''g_size = 0
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


p = Panel(menu_str, title='MENU', style='#ffdddd', width=g_size*2)
Console().print(p)'''


# MENU FUNCIONAL, MELHORAR A APARENCIA E COLOCAR O PROMPT
import colors
p = Panel.fit(
            'dfjkdkdkfkfdkfdkf=========1\ndkfkhdkfkgkdfkgdfg========2',
            padding=(1, 2),
            title="[b white]Menu",
            border_style=colors.THEME_COLORS.get('sea'),
        )
# Console().print(p, justify='center')

from rich.markdown import Markdown

md = """# Titulo md"""
# Console().print(Markdown(md, ))
from rich import box

p = Panel(Text('Login', justify='center', style='b'), box=box.DOUBLE, width=36)


# Console().print(p)

'''
.ooo.
o   o. .ooo.   ooo.    ooo.  .ooo   oo.   oo.  o   .ooo.  ooo.    ooo.
o      o   o   o   o   o     o     o     o     .   o   o  o   o  o
o      o   o   o   o   oo.   ooo   .oo.  .oo.  o   o   o  o   o  .ooo.
o  .o  o   o   o   o   o     o        o     o  o.  o   o  o   o      o
 ooo    ooo    o      .o     .ooo   oo    oo    o   ooo   o       ooo
                      o 
'''
# Console().print(c, justify='center')


from colors import TITLE, ASCEND
from random import choice


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
    sty_title = Text()
    if not blend: # no blend
        for line in TITLE:
            l = Text()
            for c in line:
                l += tint(c, ASCEND[theme])
            sty_title = sty_title + l + Text('\n')
        sty_title = sty_title[:-1] 

    else: #with blend
        n_line = 0
        for line in TITLE:
            l = Text()
            if n_line < 3:
                for c in line:
                    l += tint(c, ASCEND[theme])
            elif n_line == 3:
                for c in line:
                    l += tint(c, ASCEND[theme] + ASCEND[theme2])
            else:
                for c in line:
                    l += tint(c, ASCEND[theme2])
            sty_title = sty_title + l + Text('\n')
            n_line += 1
        sty_title = sty_title[:-1] 
    Console().print(sty_title)


display_title('rose', blend=True, theme2='violet')


# t   l
# 7   7
THEME = ''
def format_title(text='ConfessionS', scale='rand', patterns=colors.MIRROR, bold=False) -> Text:
    """
    Retuns the string in text in rich format, colored in a color scale pattern of the given color.  
    color variants : sky, sea, gold, rose, violet. Defaults to rand (random)
    """
    # palavra de tamanho 9 (talvez implementar para funcionar qualquer tamanho)
    global THEME
    # choose a random pattern
    if scale == 'rand':
        p = THEME
        
    else:
        if scale not in patterns.keys():
            Console().print(f'error - scale {scale} is not avaliable')        
            return 
        p = scale
        
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
    console.print('[bold]Welcome to[/bold]', end=' ', justify="center")
    for c in ftitle:
        console.print(c, end='', justify="center")
        time.sleep(pause)
    print()
