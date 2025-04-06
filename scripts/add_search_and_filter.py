from pathlib import Path
import re

import re

def detect_job_type(title: str) -> str:
    title_lower = title.lower()

    if "research engineer" in title_lower:
        return "Research Engineer"
    elif "postdoc" in title_lower or "postdoctoral" in title_lower:
        return "Postdoc/Researcher"
    elif re.search(r'\bphd\b', title_lower) or (
         "doctoral" in title_lower and "postdoctoral" not in title_lower):
        return "PhD"
    elif "researcher" in title_lower:
        return "Postdoc/Researcher"
    elif "lecturer" in title_lower or "professor" in title_lower:
        return "Lecturer/Professor"
    else:
        return "Other"


def process_md_file(md_file: Path):
    content = md_file.read_text(encoding="utf-8")

    # Skip if already processed
    if 'id="filterType"' in content or 'id="jobFilter"' in content:
        print(f"⚠️  Skipping {md_file.name} (already contains search/filter UI)")
        return

    lines = content.strip().splitlines()
    title_line = lines.pop(0) if lines[0].startswith('# ') else ""

    job_blocks = []
    current_block = []
    job_type = None

    for line in lines:
        if line.strip().startswith("<h3>"):
            if current_block:
                job_blocks.append((job_type, current_block))
                current_block = []

            title_text = re.sub(r"<\/?h3>", "", line).strip()
            job_type = detect_job_type(title_text)

        current_block.append(line)

    if current_block:
        job_blocks.append((job_type, current_block))

    # UI: Dropdown + Search Box
    filter_ui = """
<div id="filters" style="margin: 1em 0;">
  <label for="filterType"><strong>Filter by Job Type:</strong></label>
  <select id="filterType" style="margin-right: 1em;">
    <option value="">Show All</option>
    <option value="PhD">PhD</option>
    <option value="Postdoc/Researcher">Postdoc/Researcher</option>
    <option value="Lecturer/Professor">Lecturer/Professor</option>
    <option value="Research Engineer">Research Engineer</option>    
    <option value="Other">Other</option>
  </select>
  <input type="text" id="jobFilter" placeholder="Search jobs..." style="padding: 0.5em; width: 50%;">
</div>

<div id="jobList">
"""

    job_divs = []
    for jt, block in job_blocks:
        joined = "\n".join(block)
        wrapped = f'<div class="job" data-type="{jt}" style="margin-bottom: 1.5em;">\n{joined}\n</div>'
        job_divs.append(wrapped)

    end_div = "</div>\n\n"

    # JS: Combined filter logic (dropdown + search)
    filter_script = """<script>
document.addEventListener("DOMContentLoaded", function () {
  const typeSelect = document.getElementById('filterType');
  const textInput = document.getElementById('jobFilter');
  const jobBlocks = document.querySelectorAll('.job');

  function updateDisplay() {
    const selected = typeSelect.value.toLowerCase();
    const query = textInput.value.toLowerCase();

    jobBlocks.forEach(job => {
      const jobType = (job.dataset.type || "").toLowerCase();
      const matchesType = !selected || jobType === selected;
      const matchesQuery = job.textContent.toLowerCase().includes(query);
      job.style.display = (matchesType && matchesQuery) ? '' : 'none';
    });
  }

  typeSelect.addEventListener('change', updateDisplay);
  textInput.addEventListener('input', updateDisplay);
});
</script>
"""

    final = (
        f"{title_line}\n\n"
        + filter_ui
        + "\n\n".join(job_divs)
        + end_div
        + filter_script
    )

    md_file.write_text(final, encoding="utf-8")
    print(f"✅ Added search and job-type filters to: {md_file.name}")

def main():
    for name in ["lund.md", "uppsala.md", "stockholm.md", "gothenburg.md", "ki.md", "kth.md", "linkoping.md", "umea.md"]:
        path = Path("content") / name
        if path.exists():
            process_md_file(path)
        else:
            print(f"❌ File not found: {name}")

if __name__ == "__main__":
    main()
