import requests
from bs4 import BeautifulSoup

url = 'https://google.com' # замените на нужный URL
response = requests.get(url) # получаем содержимое страницы
soup = BeautifulSoup(response.text, 'html.parser') # используем BeautifulSoup для парсинга HTML

# ищем тег <title> и выводим его содержимое
title_tag = soup.find('title')
print(title_tag.string)

# ищем все ссылки на странице и выводим их
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
