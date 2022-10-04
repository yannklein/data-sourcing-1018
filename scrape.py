from urllib import request
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/list/ls055386972/'

response = requests.get(url, headers={'Accept-Language': 'en-US'})

# print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.find('h1').string)
movies_info = []
movies = soup.find_all('div', class_='lister-item-content')

for movie in movies:
    title = movie.find('h3').find('a').string
    duration = int(movie.find('span', class_='runtime').string.strip(' min'))
    movie_info = {
        'title': title,
        'duration': duration
    }
    movies_info.append(movie_info)

print(movies_info)