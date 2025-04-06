# swedjobs/fetcher.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

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
