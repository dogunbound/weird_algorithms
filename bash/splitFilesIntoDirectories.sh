#! /bin/bash
set -m


if [ $1 -le 0 ]
then
  echo "program must be called like so:"
  echo "bash splitFilesIntoDirectories.sh <number of files per split directory> <folder with files containing needed split"
  exit 1
fi

NumOfFilesPerDirectory=$1

if [[ -d $2 ]]; then
  echo "Entering directory $2"
else
  echo "$2 is not a directory"
  exit 1
fi

cd $2

shopt -s nullglob
files=(*)
NumOfFiles=$(ls | wc -l)
NumOfFolders=$(((NumOfFiles+NumOfFilesPerDirectory-1)/NumOfFilesPerDirectory))

echo "Splitting files in $2 into $NumOfFolders folders"

declare -a folderNames

for ((i=0; i<$NumOfFolders; i++)); do
  folderName="splitFilesIntoDirectories_folder$i"
  if [ -d "$folderName" ]; then rm -Rf $folderName; fi
  mkdir $folderName
  folderNames+=($folderName)
done

for ((i=0; i<NumOfFiles; i++)); do
  mv ${files[$i]} ${folderNames[$((i / NumOfFilesPerDirectory))]}
done
