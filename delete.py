#!/usr/bin/env python3
 
import os 
from pathlib import Path

def del_ops():
  os.chdir("/home/paul-njoroge/COPIED")

  files=["greet.txt","welcome.txt","hell.txt"]
  for file in files:
    with open(file,"w") as f1:
     f1.write("Hello everybody here\n")
  
    with open(file) as f1:
     cont=f1.read()
     print(cont)

  print(os.getcwd())

  os.chdir("/home/paul-njoroge/SCRIPTS")
  for filename in os.listdir("/home/paul-njoroge/SCRIPTS"):
      if filename.endswith(".txt"):
        os.unlink(filename)
