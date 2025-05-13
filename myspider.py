
import scrapy

class OGPSpider(scrapy.Spider):
    name = 'ogpspider'
    start_urls = ['https://ogp.me/']

    def parse(self, response):
        for title in response.css('h2'):
            yield {'title': title.css('a::text').get()}

        # for next_page in response.css('a.next'):
        #     yield response.follow(next_page, self.parse)

