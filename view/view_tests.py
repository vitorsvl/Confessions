from turtle import width
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
print(colors.THEME_COLORS.get('sky'))
Console().print(p, justify='center')

from rich.markdown import Markdown

md = """# Titulo md"""
Console().print(Markdown(md, ))
from rich import box

p = Panel(Text('Login', justify='center', style='b'), box=box.DOUBLE, width=36)


Console().print(p)