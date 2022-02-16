import os
from datetime import datetime
from typing import Iterable, List


def get_dir_path(user=None) -> str:
    """
    Return the path to the dir where exports will be saved
    """
    # getting the path of program's parent folder
    cwd = os.getcwd() # current working directory
    parent_dir = os.path.abspath(os.path.join(cwd, os.pardir)) # path to dir where the project is saved
    dir_name = "confessions data"
    path = os.path.join(parent_dir, dir_name) # path to confessions data dir, where the exports will be saved
    if user:
        path = os.path.join(path, user + '.txt')
        
    return path

def save_export(export_str: str, username: str):
    """
    Save an export of a user's confessions to text file
        export_str : string literal containing the confessions in appropriate format
        username : string containing the username of the confessions's author 
    """
    path_to_dir = get_dir_path()
    file_name = username + ".txt" # create a name like username.txt, so the file is overwritten everytime the user make a new export 
    path_to_file = os.path.join(path_to_dir, file_name)
    with open(path_to_file, "w") as file:
        file.write(export_str)

    
def nearest_char(s: str, pivot: int, char=' ') -> int:
    """
    Return the index of the nearest specified char in the string, relative to the pivot (center)
    Default char is blank space
    """
    first, last = 0, len(s) - 1
    if s[pivot] == char: return pivot
    else:
        right = pivot + 1
        left = pivot - 1
        while right <= last and left >= first:
            
            if s[right] == char: return right
            if s[left] == char: return left
            right += 1
            left -= 1

        if right > last: # reached end of string  
            while left >= first: # look only in the left
                if s[left] == char: return left
                left -= 1

        elif left < first: # reached the first char of string  
            while right <= last: # look only in the right
                if s[right] == char: return right
                right += 1

        else: return None # char was not found in string


def str_replace_at_index(s: str, indexes: Iterable, char: str) -> str:
    """
    Replace the char in the specified positions of the str with the given char
    """
    l = list(s)
    for i in indexes:
        l[i] = char
    return str().join(l)


def text_splitlines(text: str, limit=90) -> str:
    """
    Divide a text into lines, using "\\n" character 
    """
    tlengh = len(text)
    if tlengh <= limit:
        return text
    else:
        ref_points = [p for p in range(limit, tlengh, limit)] # reference points based on line len limit
        split_points = [nearest_char(text, point) for point in ref_points] # getting the nearest blank spaces to the ref points
        text_sl = str_replace_at_index(text, split_points, '\n') # replacing the determined blank spaces with \n
        return text_sl
 

def generate_export_str(conf_list: List) -> str:
    """
    Return a list of confessions in str to export format
    """
    datetime_format = "%d/%m/%Y, %H:%M" # Default format for datetime output
    export_str = ''

    for c in conf_list:
        dt = datetime.fromisoformat(c["time"])
        dt = dt.strftime(datetime_format) # datetime str

        export_str = export_str + dt + "\n\n"
        conf_text = text_splitlines(c["text"])
        export_str = export_str + conf_text + "\n\n\n" # remove 3 last \n 
    return export_str                 


def export_confessions(confessions: List, username: str):
    """
    Export confessions to text file 
    """
    e = generate_export_str(confessions)
    save_export(e, username)


if __name__ == "__main__":
            
    s = """follow mens eyes as they look to the skies 
    the shifting shafts of shining 
    weave the fabric of their dreams"""

    a = "aaa bbb ccc ddd eee fff rrr sss xxx zzz hhh ggg ttt rrr www qqq sss"
    z = 'The Oregon Dunes National Recreation Area is located on the Oregon Coast, stretching approximately 40 miles (64 km) north of the Coos River in North Bend to the Siuslaw River in Florence, and adjoining Honeyman State Park on the west. It is part of Siuslaw National Forest and is administered by the United States Forest Service.'


    cl = [
        {"text": "o o o my god", "time": datetime.now().isoformat()},
        {"text": "whats happening to me?", "time": datetime.now().isoformat()},
        {"text": "Walking down montana o o o", "time": datetime.now().isoformat()},
        {"text": "Im doing a great job here", "time": datetime.now().isoformat()},
        {"text": z, "time": datetime.now().isoformat()}
    ]
        
    e = generate_export_str(cl)
    print(e)
    save_export(e, 'User')