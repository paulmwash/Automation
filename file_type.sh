#!/bin/bash
#This code prompts user for input file 
#stores it in a variable 
#checks if file exists if exists
#its checks its type


echo "Enter file to determine its type"
read -p "Enter file " file

if [[ -z $file ]];then
  echo "You did not enter anything "

elif [[ -r $file ]];then
 echo "$file is readable"

elif [[ -w $file ]];then
  echo "$file is  writable"

elif [[ -x $file ]];then
  echo "$file is executable" 
else
  echo "Enter a valid file"
fi
