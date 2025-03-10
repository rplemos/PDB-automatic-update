import os
from datetime import date

today = date.today().strftime("%Y-%m-%d")

# Function to collect all existing PDB file names in your local directories
def get_existing_pdb_files():
    root_dir = "/hd/PDB_proteins"
    pdb_files = set()
    
    # Walk through all files in root_dir and collect PDB codes
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".cif"):
                pdb_code = filename[:4].upper()  # Get the first 4 characters of the filename as the PDB code
                pdb_files.add(pdb_code)
    
    return pdb_files

# Get all current PDB IDs from the previously fetched file
with open(f"/hd/new/new_ids/new_ids_{today}.txt", "r") as f:
    current_pdb_ids = set(line.strip() for line in f)

# Get all existing PDB files in your local directory
existing_pdb_files = get_existing_pdb_files()

# Find the missing PDB IDs
missing_pdb_ids = current_pdb_ids - existing_pdb_files

# Save missing PDB IDs to a file for downloading
with open(f"/hd/new/missing_ids/missing_ids_{today}.txt", "a") as f:
    for pdb_id in missing_pdb_ids:
        f.write(f"{pdb_id}\n")

try:
    if len(missing_pdb_ids) != 0:
        print(f"Found {len(missing_pdb_ids)} missing PDB files.\n")
    else:
        raise ValueError("No files to download! \n")
except ValueError as e:
    print(str(e))
    raise SystemExit(1)
print("---------------------------------------\n")

