import requests

isbn = '0-7475-3269-9'
bibkeys = f'ISBN:{isbn}'

# 'https://openlibrary.org/api/books?bibkeys=ISBN:0-7475-3269-9&format=json&jscmd=data'

url = "https://openlibrary.org/api/books"

reponse = requests.get(url, params={'bibkeys': bibkeys, 'format': 'json', 'jscmd': 'data'}).json()

print(reponse[bibkeys]['title'])