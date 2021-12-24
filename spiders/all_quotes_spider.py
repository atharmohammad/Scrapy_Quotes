import scrapy

class AllQuotesSpider(scrapy.Spider):
    name = "all_quotes_spider"
    
    def start_requests(self):
        url = "https://quotes.toscrape.com/tag/love/"
        yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self,response):
        quotes = response.css('div.quote')
        for q in quotes:
            text = quotes.css('span.text::text').get()
            author = quotes.css('span').css('small.author::text').get()
            tags = quotes.css('div.tags').css('a.tag::text').get()
            obj = {
                'text' : text,
                'author' : author,
                'tags' : tags
            }
            yield obj
        
        next_url = response.xpath('/html/body/div/div[2]/div[1]/nav/ul/li/a/@href').get()
        if next_url is not None:
            next_page = response.urljoin(next_url)
            yield scrapy.Request(url=next_page,callback=self.parse)