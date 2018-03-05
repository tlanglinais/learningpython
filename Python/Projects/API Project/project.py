from random import randrange
import requests

url = 'https://www.icanhazdadjoke.com/search'

topic = input('Let me tell you a joke! Give me a topic: ')
print(topic)
res = requests.get(
	url,
	headers={'Accept': 'application/json'},
	params={'term': topic}
)

data = res.json()
length = len(data['results'])

if length > 1:
	# print('length > 1: ')
	print(f"I've got {length} jokes about {topic}. Here's one: ")
	print(data['results'][randrange(length)]['joke'])

elif length == 1:
	# print('length = 1')
	print(f"I've got one joke about {topic}. Here's one: ")
	print(data['results'][0]['joke'])

else:
	# print('No match')
	print(f"Sorry I don't have any jokes about {topic}. Please try again")