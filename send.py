#!/usr/bin/env python3

import send2trash,os

def send_to_trash():
  os.chdir("/home/paul-njoroge/COPIED") #Relplace with your location

  for file in os.listdir('.'):
     send2trash.send2trash(file)

  print(os.listdir('.'))
