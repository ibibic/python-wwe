from bs4 import BeautifulSoup
import requests

wiki_url = 'https://en.wikipedia.org/wiki/List_of_WWE_personnel'
response = requests.get(wiki_url)
soup = BeautifulSoup(response.content, 'html.parser')
tb = soup.find_all('table', class_='wikitable sortable')

for table in tb:
    for link in table.find_all('span', class_='fn'):
        name = link.find('a')
        if(name==None):
            continue
        title = name.get_text('title').replace(' ', '_')
        with open(f"{title}.py", 'w') as f: 
            f.write("from bs4 import BeautifulSoup\n"
                    "import requests\n"
                    "import pprint\n"

                    'url = f"https://en.wikipedia.org/wiki/{title}"\n'

                "html_text = requests.get(url).text\n"
                "soup = BeautifulSoup(html_text, 'lxml')\n"

                "reigns_object = {}\n"
                "reigns_keys = soup.find_all('h2')\n"

                "for tag in reigns_keys:\n "
                    "if len(tag.find_next_siblings('p')) > 0:\n  "
                    "reigns_object[f'{tag.text}'] = tag.find_next_siblings('p')[0].text\n"
            )
            
            
           