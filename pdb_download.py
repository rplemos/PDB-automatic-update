from Bio.PDB import PDBList
from datetime import date

today = date.today().strftime("%Y-%m-%d")

with open(f"/hd/new/missing_ids/missing_ids_{today}.txt", "r") as file:
    pdb_identifiers = file.read().strip().split('\n')

pdb_codes = [pdb.strip() for pdb in pdb_identifiers]

pdb_list = PDBList()

pdb_list.download_pdb_files(pdb_codes, pdir=f"/hd/new/new_files/new_files_{today}", overwrite=False)

print("Missing PDB files downloaded successfully.\n")
print("------------------------------------------\n")
