from swedjobs.fetcher import fetch_html
from swedjobs.parser import parse_jobs_lund, parse_jobs_uppsala

def main():
    universities = [
        {
            "name": "Lund University",
            "url": "https://www.lunduniversity.lu.se/vacancies",
            "html_file": "html_cache/latest_lund_page.html",
            "output_md": "docs/lund.md",
            "parser": parse_jobs_lund,
        },
        {
            "name": "Uppsala University",
            "url": "https://www.uu.se/en/about-uu/join-us/jobs-and-vacancies",
            "html_file": "html_cache/latest_uppsala_page.html",
            "output_md": "docs/uppsala.md",
            "parser": parse_jobs_uppsala,
        }
    ]

    for uni in universities:
        print(f"Processing {uni['name']}...")

        # Fetch HTML
        fetch_html(uni["url"], save_to=uni["html_file"])

        # Parse jobs
        jobs = uni["parser"](uni["html_file"])

        # Write to Markdown
        with open(uni["output_md"], "w", encoding="utf-8") as f:
            f.write(f"# {uni['name']}\n\n")
            for job in jobs:
                f.write(f"## {job['title']}\n")
                f.write(f"- **Link:** [View job posting]({job['url']})\n")
                f.write(f"- **Department:** {job['department']}\n")
                f.write(f"- **Published:** {job['published']}\n")
                f.write(f"- **Deadline:** {job['deadline']}\n\n")

if __name__ == "__main__":
    main()
