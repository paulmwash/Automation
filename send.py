#!/usr/bin/env python3

import send2trash,os

os.chdir("/home/paul-njoroge/COPIED")

for file in os.listdir('.'):
   send2trash.send2trash(file)

print(os.listdir('.'))


