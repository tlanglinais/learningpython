# http://books.toscrape.com/

import scrapy

class BookSpider(scrapy.Spider):
	name = 'bookspider'
	start_urls = ['http://books.toscrape.com']

	def parse(self, response):
		for article in response.css('article.product_pod'):
			field {
				'price': article.css(".price_color::text")
				'title':
			}