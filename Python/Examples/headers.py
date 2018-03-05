import requests
url = 'https://www.icanhazdadjoke.com'

# res = requests.get(url, headers={'Accept': 'text/html'})
res = requests.get(url, headers={'Accept': 'application/json'})

data = res.json()

print(data)
# print(data['joke'])