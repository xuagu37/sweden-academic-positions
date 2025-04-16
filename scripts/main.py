from swedjobs.fetcher import fetch_html, fetch_all_pages_ki
from swedjobs.parser import (
    parse_jobs_lund, parse_jobs_uppsala, parse_jobs_stockholm, parse_jobs_gothenburg,
    parse_jobs_ki, parse_jobs_kth, parse_jobs_linkoping, parse_jobs_umea,
    parse_jobs_orebro, parse_jobs_lulea, parse_jobs_malmo, parse_jobs_chalmers, parse_jobs_slu, parse_jobs_karlstad, parse_jobs_sodertorn
)
from swedjobs.process import (
    convert_md_headings_to_html, add_search_and_filter,
    update_index_date, add_position_count
)
from pathlib import Path

def main():
    universities = [
        {
            "name": "Lund University",
            "url": "https://www.lunduniversity.lu.se/vacancies",
            "html_file": "html_cache/latest_lund_page.html",
            "raw_md": "raw_md/lund.md",
            "processed_md": "content/lund.md",
            "fetcher": fetch_html,
            "parser": parse_jobs_lund,
        },
        {
            "name": "Uppsala University",
            "url": "https://www.uu.se/en/about-uu/join-us/jobs-and-vacancies",
            "html_file": "html_cache/latest_uppsala_page.html",
            "raw_md": "raw_md/uppsala.md",
            "processed_md": "content/uppsala.md",
            "fetcher": fetch_html,
            "parser": parse_jobs_uppsala,
        },
        {
            "name": "Stockholm University",
            "url": "https://su.varbi.com/en/what:findjob/?showresult=1&categories=1&checklist=1&orglevel=1&ref=1&nologin=1&nocity=1&nocounty=1&nocountry=1&nolocalefield=1&nolocalegroup=1&hideColumns=town&norefsearch=1",
            "html_file": "html_cache/latest_stockholm_page.html",
            "raw_md": "raw_md/stockholm.md",
            "processed_md": "content/stockholm.md",
            "fetcher": fetch_html,
            "parser": parse_jobs_stockholm,
        },
        {
            "name": "Gothenburg University",
            "url": "https://www.gu.se/en/work-at-the-university-of-gothenburg/vacancies",
            "html_file": "html_cache/latest_gothenburg_page.html",
            "raw_md": "raw_md/gothenburg.md",
            "processed_md": "content/gothenburg.md",
            "fetcher": fetch_html,
            "parser": parse_jobs_gothenburg,
        },
        {
            "name": "Karolinska Institute",
            "url": "https://ki.se/en/vacancies?page=",
            "html_file": "html_cache/latest_ki_page.html",
            "raw_md": "raw_md/ki.md",
            "processed_md": "content/ki.md",
            "fetcher": fetch_all_pages_ki,
            "parser": parse_jobs_ki,
        },
        {
            "name": "KTH",
            "url": "https://www.kth.se/lediga-jobb?l=en",
            "html_file": "html_cache/latest_kth_page.html",
            "raw_md": "raw_md/kth.md",
            "processed_md": "content/kth.md",
            "fetcher": fetch_html,
            "parser": parse_jobs_kth,
        },
        {
            "name": "Linköping University",
            "url": "https://liu.se/en/work-at-liu/vacancies",
            "html_file": "html_cache/latest_linkoping_page.html",
            "raw_md": "raw_md/linkoping.md",
            "processed_md": "content/linkoping.md",
            "fetcher": fetch_html,
            "parser": parse_jobs_linkoping,
        },
        {
            "name": "Umeå University",
            "url": "https://www.umu.se/en/work-with-us/open-positions/",
            "html_file": "html_cache/latest_umea_page.html",
            "raw_md": "raw_md/umea.md",
            "processed_md": "content/umea.md",
            "fetcher": fetch_html,
            "parser": parse_jobs_umea,
        },
        {
            "name": "Örebro University",
            "url": "https://www.oru.se/english/career/available-positions",
            "html_file": "html_cache/latest_orebro_page.html",
            "raw_md": "raw_md/orebro.md",
            "processed_md": "content/orebro.md",
            "fetcher": fetch_html,
            "parser": parse_jobs_orebro,
        },
        {
            "name": "Luleå University",
            "url": "https://www.ltu.se/en/about-the-university/work-with-us/job-vacancies",
            "html_file": "html_cache/latest_lulea_page.html",
            "raw_md": "raw_md/lulea.md",
            "processed_md": "content/lulea.md",
            "fetcher": fetch_html,
            "parser": parse_jobs_lulea,
        },
        {
            "name": "Malmö University",
            "url": "https://mau.se/en/about-us/job-offers/current-vacancies/",
            "html_file": "html_cache/latest_malmo_page.html",
            "raw_md": "raw_md/malmo.md",
            "processed_md": "content/malmo.md",
            "fetcher": fetch_html,
            "parser": parse_jobs_malmo,
        },
        {
            "name": "Chalmers University of Technology",
            "url": "https://web103.reachmee.com/ext/I003/304/main?site=5&validator=a72aeedd63ec10de71e46f8d91d0d57c&lang=UK&ref=https%3A%2F%2F",
            "html_file": "html_cache/latest_chalmers_page.html",
            "raw_md": "raw_md/chalmers.md",
            "processed_md": "content/chalmers.md",
            "fetcher": fetch_html,
            "parser": parse_jobs_chalmers,
        },
        {
            "name": "Swedish University of Agricultural Sciences",
            "url": "https://web103.reachmee.com/ext/I017/1114/main?site=7&validator=87e4b706891e51f731ed44be28da8352&lang=UK&ref=https%3a%2f%2fwww.overleaf.com%2f",
            "html_file": "html_cache/latest_slu_page.html",
            "raw_md": "raw_md/slu.md",
            "processed_md": "content/slu.md",
            "fetcher": fetch_html,
            "parser": parse_jobs_slu,
        },
        {
            "name": "Karlstad University",
            "url": "https://kau.varbi.com/en/what:iframe/login:1/buttons:1/subscribe:1/template:default",
            "html_file": "html_cache/latest_karlstad_page.html",
            "raw_md": "raw_md/karlstad.md",
            "processed_md": "content/karlstad.md",
            "fetcher": fetch_html,
            "parser": parse_jobs_karlstad,
        },
        {
            "name": "Södertörn University",
            "url": "https://web103.reachmee.com/ext/I007/532/main?site=24&validator=2f5f4343b7f80edb4b210427ef968f34&lang=UK&ref=https%3a%2f%2fwww.overleaf.com%2f",
            "html_file": "html_cache/latest_sodertorn_page.html",
            "raw_md": "raw_md/sodertorn.md",
            "processed_md": "content/sodertorn.md",
            "fetcher": fetch_html,
            "parser": parse_jobs_sodertorn,
        }                                      
    ]

    for uni in universities:
        print(f"\nScraping jobs for {uni['name']}...")
        uni["fetcher"](uni["url"], save_to=uni["html_file"])

        jobs = uni["parser"](uni["html_file"])

        with open(uni["raw_md"], "w", encoding="utf-8") as f:
            f.write(f"# {uni['name']}\n\n")
            for job in jobs:
                f.write(f"### {job['title']}\n")
                f.write(f"- **Link:** [View job posting]({job['url']})\n")
                f.write(f"- **Department:** {job['department']}\n")
                f.write(f"- **Published:** {job['published']}\n")
                f.write(f"- **Deadline:** {job['deadline']}\n\n")

        print(f"Processing jobs for {uni['name']}...")
        convert_md_headings_to_html(uni["raw_md"], uni["processed_md"])
        add_search_and_filter(Path(uni["processed_md"]))
        add_position_count(uni["processed_md"]) 

    update_index_date()
    print("\nAll universities processed successfully!")

if __name__ == "__main__":
    main()


# How to find the real URL for some universities
# Right click "Develop Tools" -- "Inspect" -- "Network" -- "Doc"