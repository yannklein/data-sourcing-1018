import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/list/ls055386972/'

# STEP 1: HTTP REQUEST
response = requests.get(url, headers={"Accept-Language": "en-US"})
html_content = response.content

# STEP 2: HTML SCRAPING
soup = BeautifulSoup(html_content, 'html.parser')

movies = []

movies_info = soup.find_all('div', class_='lister-item-content')
for movie_info in movies_info:
    title = movie_info.find('h3', class_='lister-item-header').find('a').string
    duration = int(movie_info.find('span', class_='runtime').string.strip(' min'))
    movies.append({'title': title, 'duration': duration})
    
print(movies)