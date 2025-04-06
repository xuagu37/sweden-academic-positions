from swedjobs.parser import parse_jobs_lund, parse_jobs_uppsala

def test_parser():
    test_file = "html_cache/latest_uppsala_page.html"
    jobs = parse_jobs_uppsala(test_file)

    print(f"\nTest complete: {len(jobs)} job(s) found.\n")

    for i, job in enumerate(jobs, 1):
        print(f"--- Job {i} ---")
        print(f"Title     : {job['title']}")
        print(f"URL       : {job['url']}")
        print(f"Department: {job['department']}")
        print(f"Published : {job['published']}")
        print(f"Deadline  : {job['deadline']}\n")

if __name__ == "__main__":
    test_parser()
