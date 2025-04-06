#!/bin/bash

set -e

echo "=== Cleaning all _build directories ==="
find . -type d -name "_build" -exec rm -rf {} +
echo "All _build directories removed."

echo "=== Removing .DS_Store files ==="
find . -name ".DS_Store" -delete
echo ".DS_Store files removed."

echo "✅ Cleanup complete."
