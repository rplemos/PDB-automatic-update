Code to:

- Query the PDB API with a custom query and two dates (normally from the last check date to today) [PDB_query.py]
- Check the missing IDs between the two dates [PDB_checkmissing.py]
- Download the missing IDs as .cif files [PDB_download.py]
- Move the downloaded files to their correspondent folders [move_files.sh]
- Wrap all the functions with status checks [wrapper.sh]
- Run all the scripts (intended to use with crontab) [run.sh]


To run, first change the folder paths in the scripts (for crontab uses, it's better to use the complete path for each one), then just use ``./run.sh``
