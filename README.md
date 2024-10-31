Code to:

- Query the PDB API with a custom query and two dates (normally from the last check date to today): [pdb_query.py](Scripts/pdb_query.py)
  - IMPORTANT: changes to the query are made here
- Check the missing IDs between the two dates: [pdb_checkmissing.py](Scripts/pdb_checkmissing.py)
- Download the missing IDs as .cif files: [pdb_download.py](Scripts/pdb_download.py)
- Move the downloaded files to their correspondent folders: [move_files.sh](Scripts/move_files.sh)
- Wrap all the functions with status checks: [wrapper.sh](Scripts/wrapper.sh)
- Run all the scripts (intended to use with crontab): [run.sh](Scripts/run.sh)

To run, first change the folder paths in the scripts (for crontab uses, it's better to use the complete path for each one), then just use `./run.sh`.

