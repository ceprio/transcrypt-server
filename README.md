# transcrypt-server
A flask server serving python files

The jspy folder contains the python files to be crossed-compiled to javascript. Just run compile.py to cross-compile everything in the path. The files will then be available from the website through http://your.site/jspy/<filename>.html.

Source maps are generated automatically so the python code can be debugged step by step in the browser.
