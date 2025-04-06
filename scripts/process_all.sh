#!/bin/bash

set -e  # Exit on error

echo "🔄 Converting Markdown headings to <hN>..."
python -m scripts.convert_headings

echo "🔍 Adding search and job type filters..."
python -m scripts.add_search_and_filter

echo "✅ All processing complete!"
