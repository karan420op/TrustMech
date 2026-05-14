import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class TeamMember:
    name: str
    role: str
    linkedin: Optional[str] = None
    twitter: Optional[str] = None
    anonymous: bool = False

@dataclass
class FundingInfo:
    round_name: str
    amount: str
    investors: List[str] = field(default_factory=list)
    date: Optional[str] = None

@dataclass
class ProjectData:
    url: str
    project_name: str
    description: str
    team: List[TeamMember] = field(default_factory=list)
    funding: List[FundingInfo] = field(default_factory=list)
    social_links: dict = field(default_factory=dict)
    red_flags: List[str] = field(default_factory=list)

def scrape_project(url: str) -> ProjectData:
    print(f"Fetching data from: {url}")
    domain = urlparse(url).netloc

    if "twitter.com" in domain or "x.com" in domain:
        return _scrape_twitter(url)
    elif "linkedin.com" in domain:
        return _scrape_linkedin(url)
    else:
        return _scrape_website(url)

def _scrape_twitter(url: str) -> ProjectData:
    handle = url.rstrip("/").split("/")[-1]
    return ProjectData(
        url=url,
        project_name=handle,
        description="",
        social_links={"twitter": url}
    )

def _scrape_linkedin(url: str) -> ProjectData:
    return ProjectData(
        url=url,
        project_name="",
        description="",
        social_links={"linkedin": url}
    )

def _scrape_website(url: str) -> ProjectData:
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else ""
        description = ""
        meta = soup.find("meta", attrs={"name": "description"})
        if meta:
            description = meta.get("content", "")

        social_links = {}
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if "twitter.com" in href or "x.com" in href:
                social_links["twitter"] = href
            elif "linkedin.com" in href:
                social_links["linkedin"] = href
            elif "github.com" in href:
                social_links["github"] = href
            elif "discord.com" in href:
                social_links["discord"] = href

        return ProjectData(
            url=url,
            project_name=title,
            description=description,
            social_links=social_links
        )

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ProjectData(url=url, project_name="", description="")
