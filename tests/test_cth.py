import requests
from bs4 import BeautifulSoup

url = "https://web103.reachmee.com/ext/I003/304/main?site=5&validator=a72aeedd63ec10de71e46f8d91d0d57c&lang=UK&ref=https%3A%2F%2F"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.select(".list-item__heading")  # update selector as needed

for job in jobs:
    title = job.get_text(strip=True)
    link = job.find("a")
    if link:
        href = link["href"]
        full_url = "https://web103.reachmee.com" + href
        print(f"Title: {title}\nURL: {full_url}\n")
