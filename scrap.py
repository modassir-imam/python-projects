import requests
from bs4 import BeautifulSoup

url = 'https://writingcenter.unc.edu/tips-and-tools/paragraphs/'
amazon_req = requests.get(url)

amazon_soup = BeautifulSoup(amazon_req.text, 'html.parser')

print(amazon_soup.prettify())

print(amazon_soup.findAll('h2'))
