import requests

url = 'https://www.icanhazdadjoke.com/search'

# res = requests.get(url, headers={'Accept': 'text/html'})
res = requests.get(
	url,
	headers={'Accept': 'application/json'},
	params={'term': 'cat', 'limit': 1}
)

data = res.json()

print(data['results'])
# print(data['joke'])