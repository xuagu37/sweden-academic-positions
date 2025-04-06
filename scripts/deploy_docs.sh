#!/bin/bash

set -e  # Exit immediately if any command fails

echo "🔄 Cleaning previous Sphinx build..."
make -C docs clean

echo "🛠️ Building Sphinx HTML..."
make -C docs html

echo "📁 Copying HTML output into docs/..."
cp -r docs/_build/html/* docs/

echo "📦 Committing updated docs to Git..."
git add docs/
git commit -m "Deploy updated Sphinx HTML for GitHub Pages" || echo "No changes to commit."
git push origin main

echo "✅ Deployment complete. Visit your GitHub Pages site."
