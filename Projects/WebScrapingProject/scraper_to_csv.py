# http://quotes.toscrape.com
import requests
from bs4 import BeautifulSoup
from time import sleep
import csv

all_quotes = []
out_file = 'out_file.csv'
base_url = 'http://quotes.toscrape.com'
url = '/page/1'

while url:
	res = requests.get(f'{base_url}{url}')
	print(f'Now Scraping {base_url}{url}...')
	soup = BeautifulSoup(res.text, 'html.parser')
	quotes = soup.find_all(class_='quote')

	for quote in quotes:
		all_quotes.append({
			'text': quote.find(class_='text').get_text(),
			'author':quote.find(class_='author'),
			'bio-link': quote.find('a')['href']
		})

	next_btn = soup.find(class_='next')
	url = next_btn.find('a')['href'] if next_btn else None
	sleep(2)



# from csv import reader, writer
# # using nested with statements
# with open('fighters.csv') as file:
# 	csv_reader = reader(file) #data never converted to list
# 	with open('screaming_fighters.csv', 'w') as file:
# 		csv_writer = writer(file)
# 		for fighter in csv_reader:
# 			csv_writer.writerow([s.upper() for s in fighter])


# # Other approach, with only 1 file open at a time
# with open('fighers.csv') as file:
# 	csv_reader = reader(file)
# 	# data converted to list and saved to variable
# 	fighters = [[s.upper() for s in row] for row in csv_reader]

with open(out_file, 'w') as file:
	writer = csv.DictWriter(file, fieldnames=['text', 'author', 'bio-link'])
	writer.writeheader()
	for quote in quotes:
		writer.writerow({
			'text': quote['text'],
			'author': quote['author'],
			'bio-link': quote['bio-link']
			})