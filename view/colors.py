"""All colors and style stuff will be stored in this file"""

### TITLE CONFESSIONS

from random import choice


l1 = '            .ooo.                                                                 '
l2 = '            o   o. .ooo.   ooo.    ooo.  .ooo   oo.   oo.  o   .ooo.  ooo.    ooo.'
l3 = '            o      o   o   o   o   o     o     o     o     .   o   o  o   o  o    '
l4 = '            o      o   o   o   o   oo.   ooo   .oo.  .oo.  o   o   o  o   o  .ooo.'
l5 = '            o  .o  o   o   o   o   o     o        o     o  o.  o   o  o   o      o'
l6 = '             ooo    ooo    o      .o     .ooo   oo    oo    o   ooo   o       ooo '
l7 = '                                  o                                               '

TITLE = [l1, l2, l3, l4, l5, l6, l7]

### DEFAULT COLORS
ERROR = '#fc3d3d'
SUCCESS =  '#3afc85'
WARNING = '#f0ba3c'

### THEMES

THEMES = {
        'seagold': {'theme1': 'sea', 'theme2': 'gold'}, # sea+gold
        'orchid': {'theme1': 'rose', 'theme2': 'violet'}, # rose+violet
        'swamp': {'theme1': 'violet', 'theme2': 'forest'}, # violet+forest
        'autumn': {'theme1': 'gold', 'theme2': 'maple'}, # gold+maple 
        'spring': {'theme1': 'rose', 'theme2': 'fields'}, # rose+fields
        'seaborn': {'theme1': 'fields', 'theme2': 'sea'}, # sea+fields
        'oceanic': {'theme1': 'sky', 'theme2': 'sea'}, # sky+sea
        'lgbt': None
}      
### PATTERNS FOR THE TITLE ConfessionS
SCALES = {
        'sky' : ['#00CCFF','#42e9f5','#0052ff','#007aff','#00a3ff','#00ccff','#83e5eb'], 
        'rose': ['#FFE1DE','#FFBDC8','#FFA8C9','#ff426e','#ff7a70','#FF63C7','#ff738c','#FFB290'],
        'violet': ['#5F0DB7','#740FCF','#8B10E7','#A511FF','#BF57FF','#CC79FF','#DA9CFF','#E7BFFF','#b127e8', '#9d4fb0'],
        'sea': ['#018777','#43d1b7','#019245','#01A857','#01BE6B','#00D482','#25EDA9','#4BF0B8','#70F3C6','#95F6D5','#BAF9E4', '#38d9ef', '#64ed98'], 
        'gold': ['#FFBE17','#FFD644','#FFE05A', '#FFE971', '#FFF187', '#ffaa00', '#ffc800', '#ffbe33', '#ffaa0d'], 
        'maple': ['#C40806','#DE300B','#EC3E1E','#FD6E10','#F79039','#F7B155','#ff482b'],
        'fields': ['#FDFC96','#E4F78F','#BFEF88','#97E47E','#00ED01','#79DC78','#87FA00','#3AF901','#00ED01'],
        'forest': ['#225801','#43A538', '#015E0C','#016D18','#007C27','#008B38','#139447','#259C55','#38A564', '#47d159', '#60ad3d']
        }
        #'rose': ['#FFABBC', '#F0766D', '#FFA49C', '#FF9EBD', '#FF89AC', '#FF765E','#FF7F64','#FF8E74','#FFA48E', '#ff5ec1'],
        #'rose': ['#FFE1DE','#FFBDC8','#FFA8C9','#ff426e','#ff7a70','#FF63C7','#ff738c','#FFB290'],
        #'sky' : ['#082687','#0058BA','#1367C8','#2776D4','#3A84DF','#4E93E9','#74B0F8','#88BDFD','#9BCAFF','#AED6FF', '#C2E2FF', '#176ffc', '#4a6acf', '#389cff'], 
        

MIRROR = {
        'sky' : ['#95AAEA','#708CE2','#2550D3', '#0032CC','#2550D3', '#708CE2','#95AAEA'], # '#0032CC'
        'sea': ['#BAF9E4','#95F6D5','#70F3C6','#4BF0B8','#25EDA9','#00D482','#25EDA9','#4BF0B8','#70F3C6','#95F6D5','#BAF9E4'], 
        'gold': ['#FFF187', '#FFE971', '#FFE05A', '#FFD644', '#FFBE17', '#FFB100', '#FFBE17', '#FFD644', '#FFE05A', '#FFE971', '#FFF187'], 
        'rose': ['#FFABBC','#FF89A1','#FF6786','#FF446B','#FF2250','#FF0035','#FF2250','#FF446B','#FF6786','#FF89A1','#FFABBC'],
        'violet': ['#E7BFFF','#DA9CFF','#CC79FF','#BF57FF','#A511FF','#8B10E7','#A511FF','#BF57FF','#CC79FF','#DA9CFF','#E7BFFF']
        }

RAINBOW = [
        ['#880101','#A60101','#C30101','#E10101','#FF0000','#FF1515','#FF2A2A','#FF3F3F','#FF5454'], # red
        ['#AE4102','#C24902','#D65001','#EB5701','#FF5E00','#FF6B15','#FF792A','#FF863F','#FF9354'], # orange
        ['#AEA302','#C2B602','#D6C901','#EBDC01','#FFEF00','#FFF11B','#FFF237','#FFF452','#FFF66E'], # yellow
        ['#015804','#016205','#016D05','#007705','#008105','#1B8F20','#379C3B','#52AA56','#6EB771'], # green
        ['#022A98','#0130B1','#0137CB','#013EE5','#0044FF','#1B58FF','#376CFF','#5280FF','#6E94FF'], # blue
        ['#210298','#2601B1','#2B01CB','#3001E5','#3500FF','#4B1BFF','#6037FF','#7652FF','#8C6EFF'], # indigo
        ['#660298','#7701B1','#8901CB','#9A01E5','#AB00FF','#B41BFF','#BD37FF','#C652FF','#CF6EFF']  # violet 
]
RAINBOW_COLORS = '#ED8E89','#F7B685','#F3EBA5','#94C691','#6cd7e0','#8c74e3','#ab58db'

THEME_COLORS = {
        'sky': '#38b1fc',
        'sea': '#55e698',
        'gold': '#f5d864',
        'rose': '#ff94a2',
        'violet': '#b43ddb',
        'maple': '#ed5334', # #c40806
        'fields': '#81d95b',
        'forest': '#3b8f3d',
        'lgbt': None
}