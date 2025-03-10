#!/bin/bash
today=$(date +"%Y-%m-%d")

for folder in /hd/new/outputs_temp/outputs_${today}/*; do

	foldername=$(basename "$folder")
	first_char=${foldername:0:1}

	if [[ "$first_char" =~ [1-9] ]]; then
		cp -r "$folder" "/hd/PDB_outputs/$first_char/"
		echo "Folder $folder copied successfully to $first_char folder."
	fi
done
