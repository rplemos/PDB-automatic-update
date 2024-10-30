#!/bin/bash

today=$(date +"%Y-%m-%d")

for file in /hd/new/new_files/new_files_${today}/*; do
    # Get the filename without the path
    filename=$(basename "$file")
    
    first_char=${filename:0:1} # Folders are the first digit of ID

    if [[ "$first_char" =~ [1-9] ]]; then
        mv "$file" "/hd/PDB_proteins/$first_char/"
	echo "File $file moved successfuly!"
    fi
done
