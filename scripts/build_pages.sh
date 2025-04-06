#!/bin/bash

set -e  # Exit on error

echo "🔄 Cleaning previous Sphinx build..."
make clean

echo "🛠️ Building site locally (optional check)..."
make html