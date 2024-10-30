#!/bin/bash

today=$(date +"%Y-%m-%d")
/hd/new/scripts/bash3.sh | tee -a /hd/new/logs/log_${today}.log
echo -e "\nDatabase update complete!\n" | tee -a /hd/new/logs/log_${today}.log
