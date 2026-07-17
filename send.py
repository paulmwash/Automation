#!/usr/bin/env python3

import send2trash,os

os.chdir("/home/paul-njoroge/COPIED") #Relplace with your location

for file in os.listdir('.'):
   send2trash.send2trash(file)

print(os.listdir('.'))


