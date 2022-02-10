from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com'
url = f'{root}/movies_letter-A'
result = requests.get(url)
content = result.text
soup = BeautifulSoup(content, 'lxml')
# soup.find('article', class_='main-article')

# pagination
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text

links = []
for page in range(1, int(last_page) + 1)[:4]:  # range [1, 92+1]
    # https: // subslikescript.com / movies_letter - A

    result = requests.get(f'{url}?page={page}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_='main-article')

    links = []
    for link in box.find_all('a', href=True):
        links.append(link['href'])
    # print(links)
    for link in links:
        try:
            print(link)
            result = requests.get(f'{root}/{link}')
            content = result.text
            soup = BeautifulSoup(content, 'lxml')

            box = soup.find('article', class_='main-article')

            title = box.find('h1').get_text()
            transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
            # print(transcript)
            with open(f'{title}.text', 'w', encoding='utf-8') as file:
                file.write(str(transcript))
        except:


            print('Link Not Working')
            print(link)
