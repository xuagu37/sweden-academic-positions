# tests/test_fetcher.py

from swedjobs.fetcher import fetch_html

def test_fetcher():
    url = "https://www.umu.se/en/work-with-us/open-positions"
    save_path = "html_cache/latest_umea_page.html"

    fetch_html(url, wait_time=5, save_to=str(save_path))

if __name__ == "__main__":
    test_fetcher()