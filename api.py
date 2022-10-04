import requests

url = "https://api.github.com/users/yannklein"
response = requests.get(url).json()

print(response["name"])