import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?'
params = {
    'q': 'Python Developer',
    'l': 'Indonesia'
}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}

res = requests.get(url, params=params, headers=headers)

def get_total_pages():
    params = {
        'q': 'Python Developer',
        'l': 'Indonesia'
    }
    
    res = requests.get(url, params=params, headers=headers)
    
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass
    
    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()
        
    # Scraping Step
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup.prettify())
    
if __name__ == '__main__':
    get_total_pages()