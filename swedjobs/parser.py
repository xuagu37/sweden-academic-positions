from bs4 import BeautifulSoup

def parse_jobs_lund(filepath: str):
    """
    Parses job listings from a saved HTML file using known class markers.

    Args:
        filepath (str): Path to the saved HTML file.

    Returns:
        List[Dict]: Parsed job entries with title, URL, department, published date, and deadline.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    jobs = []

    # Look for all <h2> tags with the title class
    for title_h2 in soup.find_all("h2", class_="vacancies-list__job--title"):
        a_tag = title_h2.find("a")
        if not a_tag:
            continue

        title = a_tag.get_text(strip=True)
        url = a_tag.get("href")
        if not url.startswith("http"):
            url = "https://www.lunduniversity.lu.se" + url

        # Look around the same <td> block
        td_parent = title_h2.find_parent("td")

        # Department
        dept_p = td_parent.find("p", class_="vacancies-list__job--dept")
        department = dept_p.get_text(strip=True) if dept_p else "N/A"

        # Date published
        published_p = td_parent.find("p", class_="vacancies-list__job--date")
        published = "N/A"
        if published_p:
            text = published_p.get_text(strip=True)
            published = text.replace("Date published:", "").strip()

        # Last application date is in the next <td>
        next_td = td_parent.find_next_sibling("td")
        deadline = "N/A"
        if next_td:
            deadline_p = next_td.find("p")
            if deadline_p:
                deadline_text = deadline_p.get_text(strip=True)
                deadline = deadline_text.replace("Last application date:", "").strip()

        jobs.append({
            "title": title,
            "url": url,
            "department": department,
            "published": published,
            "deadline": deadline
        })

    return jobs

def parse_jobs_uppsala(filepath: str):
    """
    Parses job listings from Uppsala University's HTML page using known class markers.

    Args:
        filepath (str): Path to the saved HTML file.

    Returns:
        List[Dict]: Parsed job entries with title, URL, department, and deadline.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    jobs = []

    rows = soup.find_all("tr")
    for row in rows:
        title_td = row.find("td", class_="pos-title")
        dept_td = row.find("td", class_="pos-subcompany")
        deadline_td = row.find("td", class_="pos-ends")

        if title_td and title_td.a:
            title = title_td.a.get_text(strip=True)
            url = title_td.a.get("href")
            department = dept_td.get_text(strip=True) if dept_td else "N/A"
            deadline = deadline_td.get_text(strip=True) if deadline_td else "N/A"

            jobs.append({
                "title": title,
                "url": url,
                "department": department,
                "published": "",  # Published not available
                "deadline": deadline
            })

    return jobs