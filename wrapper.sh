#!/bin/bash

today=$(date +"%Y-%m-%d")
logfile="/hd/new/logs/log_${today}.log"

# Run each task sequentially, logging output and exiting on failure
echo -e "\n----------------------------------------------------" | tee -a "$logfile"
echo "| Starting sequence at $(date) |" | tee -a "$logfile"
echo -e "----------------------------------------------------\n" | tee -a "$logfile"

echo "Querying PDB API..." | tee -a "$logfile"
python3 /hd/new/scripts/pdb_query.py >> "$logfile" 2>&1
if [ $? -ne 0 ]; then
  echo "API query failed. Exiting." | tee -a "$logfile"
  exit 1
fi

echo "Checking missing IDs..." | tee -a "$logfile"
python3 /hd/new/scripts/pdb_checkmissing.py >> "$logfile" 2>&1
if [ $? -ne 0 ]; then
  echo "Missing IDs check failed. Exiting." | tee -a "$logfile"
  exit 1
fi

echo "Download new PDB files..." | tee -a "$logfile"
python3 /hd/new/scripts/pdb_download.py >> "$logfile" 2>&1
if [ $? -ne 0 ]; then
  echo "New files download failed. Exiting." | tee -a "$logfile"
  exit 1
fi

echo "Moving files..." | tee -a "$logfile"
/hd/new/scripts/move_files.sh >> "$logfile" 2>&1
if [ $? -ne 0 ]; then
  echo "File move operation failed. Exiting." | tee -a "$logfile"
  exit 1
fi

# This is just to remove residual files
echo "Removing obsolete files..." | tee -a "$logfile"
rm -r /hd/new/obsolete/ >> "$logfile" 2>&1
if [ $? -ne 0 ]; then
  echo "Failed to remove obsolete files. Exiting." | tee -a "$logfile"
  exit 1
fi

echo "All tasks completed successfully at $(date)." | tee -a "$logfile"

