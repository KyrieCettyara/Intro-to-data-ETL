#!/bin/bash

echo "========== Start dbt with Luigi Orchestration Process =========="

# Set Python script
PYTHON_SCRIPT="./elt.py"

# Get Current Date
current_datetime=$(date '+%d-%m-%Y_%H-%M')

# Append Current Date in the Log File
LOG_FILE="./logs/elt/elt_$current_datetime.log"

# Run Python Script and Insert Log
python "$PYTHON_SCRIPT" >> "$LOG_FILE" 2>&1

echo "========== End of dbt with Luigi Orchestration Process =========="