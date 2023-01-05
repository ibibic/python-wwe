from bs4 import BeautifulSoup
import requests
import pprint
url = f"https://en.wikipedia.org/wiki/{title}"
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
reigns_object = {}
reigns_keys = soup.find_all('h2')
for tag in reigns_keys:
 if len(tag.find_next_siblings('p')) > 0:
  reigns_object[f'{tag.text}'] = tag.find_next_siblings('p')[0].text
