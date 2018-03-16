# from bs4 import BeautifulSoup
# html = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
# 	<meta charset="UTF-8">
# 	<title>First HTML Page</title>
# </head>
# <body>
# 	<div id="first">
# 		<h3 data-example="yes">hi</h3>
# 		<p>more text.</p>
# 	</div>
# 	<ol>
# 		<li class="special">This list item is special.</li>
# 		<li class="special">This list item is also special.</li>
# 		<li>This list item is not special.<li>
# 	</ol>
# 	<div>bye</bye>
# </body>
# </html>
# """

# soup = BeautifulSoup(html, 'html.parser')

# print(soup.body)
# print(soup.find('div'))
# print(soup.find_all('div'))

# first = soup.find(id="first")
# classes = soup.find_all(class_="special")

# d = soup.find_all(attrs={'data-example': 'yes'})
# print(d)

# # Select elements by attribute
# # find an element with an id of foo
# soup.find(id='foo')
# soup.select('.bar')

# # find all elements with a class of bar
# # careful! 'class' is a reserved word in python
# soup.find_all(class_='bar')
# soup.select('.bar')

# # find all elements with a data
# # attribute of 'baz'
# # using the general attrs kwarg
# soup.find_all(attrs={'data-baz': True})
# soup.select('[data-baz]')

# soup = BeautifulSoup(html, 'html.parser')
# el = soup.select('.special')[0]
# print(el.get_text())
# print(el.name)
# print(el.attrs)

# attr = soup.find('div')['id']

# soup = BeautifulSoup(html, 'html.parser')
# # data = soup.body.contents[1].next_sibling.next_sibling
# # data = soup.find(class_='super-special').parent.parent
#  data = soup.find(class_='super-special').find_next_sibling(class_='special')

#  data = soup.find('h3').find_parent()

# <---First Project--->
import requests
from bs4 import BeautifulSoup
import csv

response = requests.get('https://www.rithmschool.com/blog')
print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('article')
# print(articles)

for article in articles:
	a_tag = article.find('a')
	title = a_tag.get_text()
	url = article.a_tag['href']
	time = article.find('time')['datetime']
	title, url, time