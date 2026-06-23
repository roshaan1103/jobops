import requests
from bs4 import BeautifulSoup


def scrape_remoteok(url: str) -> str:
    """
    Extract job description from RemoteOK job pages.
    RemoteOK is relatively simple HTML so this works well.
    """

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove noise
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()

        # RemoteOK usually puts job description inside article/body sections
        main_content = soup.find("div", {"class": "description"}) or \
                       soup.find("div", {"class": "details"}) or \
                       soup.find("article")

        if main_content:
            text = main_content.get_text(separator="\n", strip=True)
        else:
            # fallback
            paragraphs = soup.find_all("p")
            text = "\n".join(p.get_text(strip=True) for p in paragraphs)

        return text.strip()

    except Exception as e:
        return f"REMOTEOK_SCRAPE_ERROR: {str(e)}"