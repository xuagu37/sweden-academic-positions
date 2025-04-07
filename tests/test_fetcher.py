# tests/test_fetcher.py

from swedjobs.fetcher import fetch_html, fetch_all_pages_ki

def test_fetcher():
    url = "https://www.chalmers.se/en/about-chalmers/work-with-us/vacancies"
    save_path = "html_cache/latest_chalmers_page.html"

    fetch_html(url, wait_time=5, save_to=str(save_path))

    # fetch_all_pages(url, wait_time=5, save_to=str(save_path))

if __name__ == "__main__":
    test_fetcher()
    