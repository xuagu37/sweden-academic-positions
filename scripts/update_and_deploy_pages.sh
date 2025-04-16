#!/bin/bash

set -e  # Exit on error

# module load Mambaforge/23.3.1-1
module load Miniforge3/24.11.3-2
mamba activate sweden-academic-positions

python -m scripts.main
bash scripts/deploy_pages.sh 

