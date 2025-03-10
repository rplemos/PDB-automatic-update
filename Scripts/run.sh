#!/bin/bash

today=$(date +"%Y-%m-%d")
conda activate
/hd/new/scripts/wrapper.sh | tee -a /hd/new/logs/log_${today}.log
echo -e "\nDatabase update complete!\n" | tee -a /hd/new/logs/log_${today}.log
