#!/bin/bash

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
