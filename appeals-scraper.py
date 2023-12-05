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
    soup = BeautifulSoup(response.content, "html.parser")

    # find the main content of the page
    main_content = soup.find("div", {"id": "content2"})

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

    # check if images are present
    if len(main_content.find_all("img")) > 0:
        # save PDF file
        style = "<style>img { max-width: 100%; }</style>"
        html = f"<html><head>{style}</head><body>{main_content}</body></html>"
        HTML(string=html, base_url=BASE_URL).write_pdf(f"{filename}.pdf")
        print(f"saved to {filename}.pdf")


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
