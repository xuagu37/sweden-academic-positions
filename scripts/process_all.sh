#!/bin/bash

set -e  # Exit on error

echo "🔄 Scraping job information..."
python -m scripts.run_scraper

echo "🔄 Converting Markdown headings to <hN>..."
python -m scripts.convert_headings

echo "🔍 Adding search and job type filters..."
python -m scripts.add_search_and_filter

echo "🔍 Updated 'Last updated' in content/index.md..."
python -m  scripts.update_index_date

echo "🔍 Updated 'Total positions' in content/university.md..."
python -m  scripts.add_position_count

echo "✅ All processing complete!"
