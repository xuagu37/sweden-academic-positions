# tests/test_fetcher.py

from swedjobs.fetcher import fetch_html, fetch_all_pages_ki

def test_fetcher():
    url = "https://web103.reachmee.com/ext/I007/532/main?site=24&validator=2f5f4343b7f80edb4b210427ef968f34&lang=UK&ref=https%3a%2f%2fwww.overleaf.com%2f"
    save_path = "html_cache/latest_sodertorn_page.html"

    fetch_html(url, wait_time=5, save_to=str(save_path))

    # fetch_all_pages(url, wait_time=5, save_to=str(save_path))

if __name__ == "__main__":
    test_fetcher()
    