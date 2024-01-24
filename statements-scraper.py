import glob
import re
import requests
from bs4 import BeautifulSoup, NavigableString
from markdownify import markdownify as md
from sys import stderr, exit
from urllib.parse import urljoin
from weasyprint import HTML

BASE_URL = 'https://www.ietf.org'
URL = f'{BASE_URL}/about/groups/iesg/statements/'


def remove_new_lines(el):
    if el.name is not None:
        for child in el.children:
            if isinstance(child, NavigableString):
                child.string.replace_with(child.get_text().strip())
            else:
                remove_new_lines(child)

def save_content(url, filename):
    '''Save content as markdown. If image is present, save the PDF as well.'''

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # find the main content of the page
    main_content = soup.find('main')

    # find and delete unwanted
    for element_type in ['nav', 'form', 'button']:
        elements = main_content.find_all(element_type)
        for element in elements:
            element.decompose()

    filter_by = main_content.find('h6')
    if filter_by:
        filter_by.decompose()

    filter_by_topic = main_content.find('h2', string='Filter by topic and date')
    if filter_by_topic:
        filter_by_topic.decompose()

    social = main_content.find('h2', string='Share this page')
    while social:
        next_element = social.nextSibling
        social.decompose()
        social = next_element

    # convert block-heading div tags to h2
    for div in main_content.find_all('div', class_='block-heading'):
        div.name = 'h2'

    # fix tables
    tables = main_content.find_all('table')
    for table in tables:

        caption = table.find('caption')
        if caption:
            p = soup.new_tag('p')
            p.string = caption.get_text().strip()
            table.insert_before(p)
            caption.decompose()
        for th in table.find_all('th'):
            remove_new_lines(th)
        for td in table.find_all('td'):
            remove_new_lines(td)

    main_content_str = str(main_content)

    # remove exesive lines
    main_content_str = '\n'.join(
        line for line in str(main_content).splitlines() if line.strip()
    )

    # fix issue with no newline before headings
    h_pattern = re.compile(r'(?<!\n)<h')
    main_content_str = h_pattern.sub('\n<h', main_content_str)

    # save markdown
    markdown = md(main_content_str)

    # preserve code blocks
    for block in ['<CODE BEGINS>', '<CODE ENDS>']:
        markdown = markdown.replace(block, f'`{block}`')

    # remove any exsive newlines in begining
    markdown = markdown.lstrip("\n")

    # write to markdown file
    with open(f'{filename}.md', 'w') as file:
        file.write(markdown)
        print(f'saved to {filename}.md')

    # check if images are present
    if len(main_content.find_all('img')) > 0:
        # save PDF file
        style = '<style>img { max-width: 100%; }</style>'
        html = f'<html><head>{style}</head><body>{main_content}</body></html>'
        HTML(string=html, base_url=BASE_URL).write_pdf(f'{filename}.pdf')
        print(f'saved to {filename}.pdf')


response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

# find minutes entries
main_content = soup.find('main')
statements = main_content.select('tr')

# process statements
for statement in statements:
    tds = statement.find_all('td')
    # get meeting date
    date = tds[0].text
    match  = re.search(r'\d{4}-\d{2}-\d{2}', date)
    if match:
        date = match.group()
    else:
        stderr.write(f'Can not determine statement date from {date}')
        exit(1)

    increment = 0
    original_date = date
    date = f'{original_date}-{increment}'
    while glob.glob(f'{date}.*'):
        increment += 1
        date = f'{original_date}-{increment}'

    print(f'processing statement on {date}')

    stement_link = urljoin(BASE_URL, tds[1].find('a')['href'])

    save_content(stement_link, date)
