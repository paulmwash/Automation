#!/usr/bin/env python3


import os

def get_size():
  total=0
  for filename in os.listdir("/home/paul-njoroge/SCRIPTS"):
     total= total + os.path.getsize(os.path.join("/home/paul-njoroge/SCRIPTS",filename))
  print(total)

if __name__=="__main__":
    get_size()
