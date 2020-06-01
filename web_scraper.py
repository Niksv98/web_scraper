import requests
from bs4 import BeautifulSoup

url1 = 'https://www.latvijasdaba.lv/'
url2 = 'http://botany.lv/'

def getLinksToScrape(url):

    page1 = requests.get(url)
    soup1 = BeautifulSoup(page1.content, 'html.parser')

    found_links = []

    # Adds all the found links in an array
    for one_a_tag in soup1.find_all('a'):
        link = one_a_tag.get('href')
        found_links.append(link)

    # Remove duplicate links from the list
    found_links = list(dict.fromkeys(found_links))

    final_links = []
    for i in found_links:
        if "http://" in i or "https://" in i:
            final_links.append(i)

    return final_links


def getTextFromLinks(link_list):
    text = ''

    # Get all the text from all the links
    for i in link_list:
        page2 = requests.get(i)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        for tag in soup2.find_all('p'):
            text += tag.get_text()

    new_file = open('link_text.txt',"w", encoding="utf8")
    new_file.write(text)

link_list = getLinksToScrape(url2)
print(link_list)

# getTextFromLinks(link_list)
