import os
import csv
import sys

contacts_file = "/hd/PDB_outputs/total_contacts.txt"

def process_contacts_csv(folder_path, ids_file, base_path, big_path):
    
    id_list = []
    big_list = []
    
    with open(contacts_file, "r") as f:
        intrachain, interchain, total, entries, _  = f.readlines()
        intrachain = int(intrachain.strip())    
        interchain = int(interchain.strip())
        total = int(total.strip())
        entries = int(entries.strip())

    print(f"Previous: {intrachain}, {interchain}, {total}, {entries}")
        
    with open(ids_file, "r") as f:
        for line in f:
            id_list.append(line.strip())
            
    with open(big_path, "r") as f:
        for line in f:
            big_list.append(line.strip()[0:4])
            
    for i, [root, dirs, files] in enumerate(os.walk(folder_path)):
        #print(i, root, dirs, files)
        for file in files:
            if file.endswith(".cif"):
                pdb_id = file[0:4].upper()
                if pdb_id not in id_list and pdb_id not in big_list:
                    #print("\t", pdb_id)
                    with open(ids_file, "a") as f:
                        f.write(f"{pdb_id}\n")

                    file_path = f"{base_path}/{pdb_id[0]}/{pdb_id}/{pdb_id}_contacts.csv"
                    
                    with open(file_path, "r", encoding="utf-8") as csv_file:
                        csv_reader = csv.reader(csv_file)
                        for line in csv_reader:
                            if line[0] == line[4]:
                                intrachain += 1
                            else:
                                interchain += 1
    
    total = intrachain + interchain
    return intrachain, interchain, total

if __name__ == "__main__":
    folder_path = sys.argv[1]
    num_ids = sys.argv[2]
    update_date = sys.argv[3]
    ids_file = "/hd/PDB_outputs/id_list.txt"
    big_path = "/hd/PDB_outputs/big.csv"
    base_path = "/hd/PDB_outputs"

    intrachain, interchain, total = process_contacts_csv(folder_path, ids_file, base_path, big_path)
    print(f"Intrachain contacts: {intrachain}")
    print(f"Interchain contacts: {interchain}")
    print(f"Total contacts: {total}")
    print(f"Total entries: {num_ids}")
    
    with open(contacts_file, "w") as f:
        f.write(f"{intrachain}\n")
        f.write(f"{interchain}\n")
        f.write(f"{total}\n")
        f.write(f"{num_ids}\n")
        f.write(f"{update_date}")
    
