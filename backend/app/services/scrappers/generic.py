import requests
from bs4 import BeautifulSoup


def scrape_generic(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(res.text, "html.parser")

    # remove junk
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()

    paragraphs = soup.find_all("p")

    text = "\n".join(p.get_text(strip=True) for p in paragraphs)

    return text.strip()