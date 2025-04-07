# swedjobs/fetcher.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

def fetch_html(url: str, wait_time: int = 8, save_to: str = None) -> str:
    """
    Fetches the fully rendered HTML content of the given URL using Selenium.
    
    Args:
        url (str): The web page URL to fetch.
        wait_time (int): Seconds to wait for JavaScript-rendered content.
        save_to (str): Optional. Path to save the HTML output locally.

    Returns:
        str: The rendered HTML.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(wait_time)
    
    html = driver.page_source
    driver.quit()

    if save_to:
        with open(save_to, "w", encoding="utf-8") as f:
            f.write(html)

    return html


def fetch_all_pages_ki(base_url: str, save_to: str = None, wait_time: int = 4, max_pages: int = 10) -> str:
    combined_html = ""
    found_any = False

    for page in range(max_pages):
        url = f"{base_url}{page}"
        print(f"🔍 Fetching page {page}: {url}")
        try:
            html = fetch_html(url, wait_time, save_to=None)
        except Exception as e:
            print(f"❌ Error on page {page}: {e}")
            break

        soup = BeautifulSoup(html, "html.parser")
        job_rows = soup.select("table tbody tr")
        titles = soup.select(".views-field-title")

        if not job_rows or not titles:
            print("🛑 No job rows or job titles found. Stopping.")
            break

        combined_html += html
        found_any = True

    if found_any and save_to:
        with open(save_to, "w", encoding="utf-8") as f:
            f.write(combined_html)
        print(f"✅ Combined HTML saved to {save_to}")
    else:
        print("⚠️ No job listings found.")

    return combined_html



