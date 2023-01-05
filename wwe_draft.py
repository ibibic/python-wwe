with open(f"{title}.py", 'w') as f: 
            f.write("from bs4 import BeautifulSoup\n"
                    "import requests\n"
                    "import pprint\n"

                    "url = 'https://en.wikipedia.org/wiki/Roman_Reigns'\n"

                "html_text = requests.get(url).text\n"
                "soup = BeautifulSoup(html_text, 'lxml')\n"

                "reigns_object = {}\n"
                "reigns_keys = soup.find_all('h2')\n"

                "for tag in reigns_keys:\n"
                    "if len(tag.find_next_siblings('p')) > 0:\n "
                    "reigns_object[f'{tag.text}'] = tag.find_next_siblings('p')[0].text\n"
            )
            