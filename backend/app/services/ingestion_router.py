from urllib.parse import urlparse

from app.services.scrappers.remoteok import scrape_remoteok
from app.services.scrappers.generic import scrape_generic


def detect_source(url: str) -> str:
    domain = urlparse(url).netloc.lower()

    if "remoteok" in domain:
        return "remoteok"

    if "weworkremotely" in domain:
        return "weworkremotely"

    if "linkedin" in domain:
        return "linkedin"

    if "indeed" in domain:
        return "indeed"

    return "generic"


def route_scraper(url: str) -> str:
    """
    Returns extracted text based on site type
    """

    source = detect_source(url)

    if source == "remoteok":
        return scrape_remoteok(url)

    if source == "linkedin":
        # blocked → fallback
        return "LINKEDIN_JOB_FALLBACK"

    if source == "indeed":
        # blocked → fallback
        return "INDEED_JOB_FALLBACK"

    return scrape_generic(url)