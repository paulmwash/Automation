#This script you can run on you command line followed by what you ant to search 
#./search.py <search-query>

#!/usr/bin/env python3

import sys,webbrowser,pyperclip

if len(sys.argv) > 1:
  search= ' '.join(sys.argv[1:])
  print(search)
else:
  search=pyperclip.paste()

webbrowser.open(f"https://www.google.com/search?q={search}")
