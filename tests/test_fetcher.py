# tests/test_fetcher.py

from swedjobs.fetcher import fetch_html

def test_fetcher():
    url = "https://su.varbi.com/en/what:findjob/?showresult=1&categories=1&checklist=1&orglevel=1&ref=1&nologin=1&nocity=1&nocounty=1&nocountry=1&nolocalefield=1&nolocalegroup=1&hideColumns=town&norefsearch=1"
    save_path = "html_cache/latest_stockholm_page.html"

    fetch_html(url, wait_time=5, save_to=str(save_path))

if __name__ == "__main__":
    test_fetcher()