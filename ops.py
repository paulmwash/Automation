#!/usr/bin/env python3


import os,shutil

def operations():
  SOURCE_DIR="/home/paul-njoroge/Documents"
  DEST_DIR="/home/paul-njoroge/MUST"

  if not os.path.exists(DEST_DIR):
    os.makedirs(DEST_DIR)
    print(f"Dir {DEST_DIR} created successful") 
  else:
    print(f"Dir {DEST_DIR} exists ")

  os.chdir(SOURCE_DIR)

  for file in os.listdir(SOURCE_DIR):
    if file.endswith(".pdf"):
     source_file=os.path.join(SOURCE_DIR,file)
     dest_file=os.path.join(DEST_DIR,file)
     shutil.copy(source_file,dest_file)
  print(os.getcwd())
