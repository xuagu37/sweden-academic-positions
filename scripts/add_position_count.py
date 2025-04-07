import re
from pathlib import Path

def add_position_count(file_path: str):
    path = Path(file_path)
    text = path.read_text(encoding="utf-8")

    # Count number of job entries
    job_count = len(re.findall(r'<div class="job"\s', text))-1

    # Prepare the counter line
    count_line = f'<p style="font-size: 1.2em; font-weight: bold;">Total positions: {job_count}</p>'

    # Insert the line after the main heading (first line starting with "# ")
    updated = re.sub(
        r"^(# .+?)\n(?!_Total positions:)",
        rf"\1\n{count_line}\n",
        text,
        count=1,
        flags=re.MULTILINE
    )

    # Replace any existing count line if present
    updated = re.sub(r"_Total positions: \d+_", count_line, updated)

    path.write_text(updated, encoding="utf-8")
    print(f"✅ Added job count to: {file_path}")

# Example usage
if __name__ == "__main__":
    add_position_count("content/lund.md")
    add_position_count("content/uppsala.md")
    add_position_count("content/stockholm.md")
    add_position_count("content/gothenburg.md")
    add_position_count("content/ki.md")
    add_position_count("content/kth.md")    
    add_position_count("content/linkoping.md")
    add_position_count("content/umea.md")
    add_position_count("content/orebro.md")
    add_position_count("content/lulea.md")
    add_position_count("content/malmo.md")
