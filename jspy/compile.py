# switches:
if 0:
    import transcrypt.modules.org.transcrypt.utils
debug = True
add = None
if debug:
    add = "-m -n"

import os
from os import listdir
from os.path import isfile, isdir, join
path = "."
onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith(".py")]

for file in onlyfiles:
    if file != "compile.py":
        os.system(f"transcrypt {add} {join(path, file)}")  
