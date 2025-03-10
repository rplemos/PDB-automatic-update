<!-- 
Code to:

- Query the PDB API with a custom query and two dates (normally from the last check date to today) [PDB_query.py]
- Check the missing IDs between the two dates [PDB_checkmissing.py]
- Download the missing IDs as .cif files [PDB_download.py]
- Move the downloaded files to their correspondent folders [move_files.sh]
- Wrap all the functions with status checks [wrapper.sh]
- Run all the scripts (intended to use with crontab) [run.sh]


To run, first change the folder paths in the scripts (for crontab uses, it's better to use the complete path for each one), then just use ``./run.sh``
-->

Currently providing only a specific case for use in the [COCaDA-Web](https://github.com/LBS-UFMG/cocada-web) tool. In the future, a more general implementation will be provided, along with a more complete documentation.

## Contact
For any questions or issues, please contact:

Rafael Pereira Lemos - PhD Student in Bioinformatics @ Federal University of Minas Gerais

Email: rafaellemos42@gmail.com

GitHub: https://github.com/rplemos
