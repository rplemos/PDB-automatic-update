import requests
import json
import time
from datetime import date, timedelta, datetime
import sys

url_search_api = 'https://search.rcsb.org/rcsbsearch/v2/query?json='
error_date = "1970-01-01"

# Read the last run date or set to a default if the file doesn't exist
try:
    with open('/hd/new/last_run_dates.txt', 'r') as f:
        lines = f.readlines()
        if lines:
            last_run_date = lines[-1].strip()
            #date_check = str(datetime.strptime(last_run_date,"%Y-%m-%d") - timedelta(days=5))
        else:
            last_run_date = error_date
except FileNotFoundError:
    last_run_date = error_date 

today = date.today().strftime("%Y-%m-%d")

# Define the base query to fetch only new entries since the last run date
query = {
    "query": {
        "type": "group",
        "logical_operator": "and",
        "nodes": [
            {
                "type": "terminal",
                "service": "text",
                "parameters": {
                    "attribute": "entity_poly.rcsb_entity_polymer_type",
                    "operator": "exact_match",
                    "value": "Protein"
                }
            },
            {
                "type": "terminal",
                "service": "text",
                "parameters": {
                    "attribute": "rcsb_accession_info.initial_release_date",
                    "operator": "greater_or_equal",
                    #"value": "1970-01-01"
                    "value": "2025-01-01"
                    #"value": last_run_date
                    #"value": date_check
                }
            },
            {
                "type": "terminal",
                "service": "text",
                "parameters": {
                    "attribute": "rcsb_accession_info.initial_release_date",
                    "operator": "less_or_equal",
                    "value": today
                }
            },
        ]
    },
    "return_type": "entry",
    "request_options": {
        "paginate": {
            "start": 0,
            "rows": 1000
        },
        "results_content_type": [
            "experimental"
        ]
    }
}

def fetch_pdb_ids(start=0, rows=1000):
    all_results = []
    total_count = 1

    while start < total_count:
        query['request_options']['paginate']['start'] = start
        url = url_search_api + json.dumps(query)
        response = requests.get(url)
        if response.status_code == 204:
            print("\nNo new files were added in this week. Exiting... \n")
            sys.exit(1)
        response.raise_for_status()
        result = response.json()

        # Extract total count from the first response
        if start == 0:
            total_count = result['total_count']
            print(f"\nTotal entries to retrieve: {total_count}")

        # Extract entries from the result
        entries = result['result_set']
        all_results.extend([entry['identifier'] for entry in entries])

        # Update start for the next batch
        start += rows
        print(f"Retrieved {len(all_results)} entries so far...")

        time.sleep(1)  # Avoid overwhelming the server

    return all_results

# Fetch PDB IDs for the new range
pdb_ids_new = fetch_pdb_ids()

# Save the new PDB IDs to a file
with open(f"/hd/new/new_ids/new_ids_{today}.txt", "a") as f:
    for pdb_id in pdb_ids_new:
        f.write(f"{pdb_id}\n")

# Update the last run date
with open('/hd/new/last_run_dates.txt', 'a') as f:
    if today != last_run_date: 
        f.write(f"{today}\n")

print("\nPDB IDs fetched and last run date updated.\n")
print("-------------------------------------------\n")
