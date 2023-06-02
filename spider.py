import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://www.t66y.com/thread0806.php?fid=7&search=&page={}'.format(i) for i in range(1, 2)]

    def parse(self, response):
        for title in response.css('h3 a::text'):
            yield {'title': title.get()}
            DOWNLOAD_DELAY = 3 # means a delay of 3 seconds between requests
