from datetime import date
from pathlib import Path
import re

def update_index_date(path="content/index.md"):
    file_path = Path(path)
    content = file_path.read_text(encoding="utf-8")

    today = date.today().isoformat()
    updated_line = f"_Last updated: {today}_"

    # Replace the line or insert if not found
    if "_Last updated:" in content:
        content = re.sub(r"_Last updated:.*_", updated_line, content)
    else:
        content = content.replace(
            "Welcome! This site presents regularly scraped academic job listings from Swedish universities.",
            f"Welcome! This site presents regularly scraped academic job listings from Swedish universities.\n\n{updated_line}"
        )

    file_path.write_text(content, encoding="utf-8")
    print(f"✅ Updated 'Last updated' in {file_path} to {today}")

if __name__ == "__main__":
    update_index_date()
