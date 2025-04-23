import sys
from urllib.parse import urlparse, parse_qs, urlencode
from html import unescape

def convert_reachmee_url(raw_url: str) -> str:
    """
    Convert a ReachMee 'main' style job URL to the working 'job' style URL.

    Args:
        raw_url (str): The original URL (may contain &amp; and use rmjob=...).

    Returns:
        str: A converted working URL, or the original if it can't be converted.
    """
    # Unescape HTML entities (&amp; → &)
    decoded_url = unescape(raw_url)
    
    # Parse URL
    parsed = urlparse(decoded_url)
    query = parse_qs(parsed.query)

    # Check if it's a main-style job link and can be converted
    if parsed.path.endswith("/main") and "rmjob" in query and "rmpage" in query and query["rmpage"][0] == "job":
        try:
            new_query = {
                "site": query["site"][0],
                "lang": query["lang"][0],
                "validator": query["validator"][0],
                "job_id": query["rmjob"][0]
            }
            new_url = f"{parsed.scheme}://{parsed.netloc}/ext/I005/1035/job?{urlencode(new_query)}"
            return new_url
        except KeyError as e:
            print(f"Missing required parameter: {e}")
            return raw_url
    else:
        return raw_url  # Return as-is if not convertible

# ---- Example usage ----

if __name__ == "__main__":
    example_url = "https://web103.reachmee.com/ext/I005/1035/main?site=7&amp;validator=9b89bead79bb7258ad55c8d75228e5b7&amp;lang=UK&amp;rmpage=job&amp;rmjob=37154"
    
    if len(sys.argv) > 1:
        example_url = sys.argv[1]
    
    fixed_url = convert_reachmee_url(example_url)
    print("Converted URL:")
    print(fixed_url)
