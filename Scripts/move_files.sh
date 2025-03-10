#!/bin/bash

today=$(date +"%Y-%m-%d")
#today="2024-12-08"

for file in /hd/new/new_files/new_files_${today}/*; do
    #echo "$file"
    # Get the filename without the path
    filename=$(basename "$file")
    
    # Get the first character of the filename
    first_char=${filename:0:1}

    # Check if the first character is a digit between 1 and 9
    if [[ "$first_char" =~ [1-9] ]]; then
        # Copy the file to the corresponding directory
        cp "$file" "/hd/PDB_proteins/$first_char/"
	echo "File $file copied successfuly! to $first_char folder."
    fi
done
