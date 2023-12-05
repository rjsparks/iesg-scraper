import re
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from sys import stderr, exit
from urllib.parse import urljoin
from weasyprint import HTML

BASE_URL = "https://www6.ietf.org"
URL = f"{BASE_URL}/iesg/appeal/"


def save_content(url, filename):
    """Save content as markdown. If image is present, save the PDF as well."""
    response = requests.get(url)
    for replacement in [b"<![if !supportEmptyParas]>", b"<![endif]>"]:
        response._content = response.content.replace(replacement, b"")
    soup = BeautifulSoup(response.content, "html.parser")

    # find the main content of the page
    main_content = soup.find("div", {"id": "content2"})
    main_content_str = str(main_content)

    # remove exesive lines
    main_content_str = "\n".join(
        line for line in str(main_content).splitlines() if line.strip()
    )

    # save markdown
    markdown = md(main_content_str)

    # write to markdown file
    with open(f"{filename}.md", "w") as file:
        file.write(markdown)
        print(f"saved to {filename}.md")


response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

# find appeals
appeals = soup.select("a")

# process appeals
for appeal in appeals:
    href = appeal.get("href")
    if href and href.endswith(".html"):
        print(f"processing appeal on {href}")
        appeal_link = urljoin(URL, href)
        save_content(appeal_link, href[:-5])
