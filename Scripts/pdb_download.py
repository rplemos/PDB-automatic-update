from Bio.PDB import PDBList
from datetime import date

today = date.today().strftime("%Y-%m-%d")
#today = "2024-10-27"

# Read missing PDB identifiers from the file
with open(f"/hd/new/missing_ids/missing_ids_{today}.txt", "r") as file:
    pdb_identifiers = file.read().strip().split('\n')

# Strip any extra whitespace from each identifier
pdb_codes = [pdb.strip() for pdb in pdb_identifiers]

# Initialize PDBList
pdb_list = PDBList()

# Download PDB files (update the folder path as needed)
pdb_list.download_pdb_files(pdb_codes, pdir=f"/hd/new/new_files/new_files_{today}", overwrite=False)

print("Missing PDB files downloaded successfully.\n")
print("------------------------------------------\n")
