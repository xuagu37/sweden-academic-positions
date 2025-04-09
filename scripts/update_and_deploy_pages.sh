#!/bin/bash

set -e  # Exit on error

module load Mambaforge/23.3.1-1
mamba activate sweden-academic-positions

python -m scripts.main
bash scripts/deploy_pages.sh 

