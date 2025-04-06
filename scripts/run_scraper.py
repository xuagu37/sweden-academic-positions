from swedjobs.fetcher import fetch_html
from swedjobs.parser import parse_jobs_lund, parse_jobs_uppsala, parse_jobs_stockholm, parse_jobs_gothenburg, parse_jobs_ki, parse_jobs_kth, parse_jobs_linkoping, parse_jobs_umea

def main():
    universities = [
        # {
        #     "name": "Lund University",
        #     "url": "https://www.lunduniversity.lu.se/vacancies",
        #     "html_file": "html_cache/latest_lund_page.html",
        #     "output_md": "html_cache/lund.md",
        #     "parser": parse_jobs_lund,
        # },
        # {
        #     "name": "Uppsala University",
        #     "url": "https://www.uu.se/en/about-uu/join-us/jobs-and-vacancies",
        #     "html_file": "html_cache/latest_uppsala_page.html",
        #     "output_md": "html_cache/uppsala.md",
        #     "parser": parse_jobs_uppsala,
        # },
        # {
        #     "name": "Stockholm University",
        #     "url": "https://su.varbi.com/en/what:findjob/?showresult=1&categories=1&checklist=1&orglevel=1&ref=1&nologin=1&nocity=1&nocounty=1&nocountry=1&nolocalefield=1&nolocalegroup=1&hideColumns=town&norefsearch=1",
        #     "html_file": "html_cache/latest_stockholm_page.html",
        #     "output_md": "html_cache/stockholm.md",
        #     "parser": parse_jobs_stockholm,
        # },
        # {
        #     "name": "Gothenburg University",
        #     "url": "https://www.gu.se/en/work-at-the-university-of-gothenburg/vacancies",
        #     "html_file": "html_cache/latest_gothenburg_page.html",
        #     "output_md": "html_cache/gothenburg.md",
        #     "parser": parse_jobs_gothenburg,
        # },
        # {
        #     "name": "Karolinska Institute",
        #     "url": "https://ki.se/en/about-ki/jobs-at-ki/available-positions-at-ki",
        #     "html_file": "html_cache/latest_ki_page.html",
        #     "output_md": "html_cache/ki.md",
        #     "parser": parse_jobs_ki,
        # },
        # {
        #     "name": "KTH",
        #     "url": "https://www.kth.se/lediga-jobb?l=en",
        #     "html_file": "html_cache/latest_kth_page.html",
        #     "output_md": "html_cache/kth.md",
        #     "parser": parse_jobs_kth,
        # },
        # {
        #     "name": "Linköping University",
        #     "url": "https://liu.se/en/work-at-liu/vacancies",
        #     "html_file": "html_cache/latest_linkoping_page.html",
        #     "output_md": "html_cache/linkoping.md",
        #     "parser": parse_jobs_linkoping,
        # },
        {
            "name": "Umeå University",
            "url": "https://www.umu.se/en/work-with-us/open-positions/",
            "html_file": "html_cache/latest_umea_page.html",
            "output_md": "html_cache/umea.md",
            "parser": parse_jobs_umea,
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
                f.write(f"### {job['title']}\n")
                f.write(f"- **Link:** [View job posting]({job['url']})\n")
                f.write(f"- **Department:** {job['department']}\n")
                f.write(f"- **Published:** {job['published']}\n")
                f.write(f"- **Deadline:** {job['deadline']}\n\n")

if __name__ == "__main__":
    main()
