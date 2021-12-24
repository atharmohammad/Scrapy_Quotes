import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/tag/love/",
            "https://quotes.toscrape.com/tag/inspirational/",
            "https://quotes.toscrape.com/tag/life/"
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self,response):
        tag = response.url.split('/')[-2]
        filename = "%s_Quotes.html"%tag
        print(f"${filename} is processing")
        with open (filename,"wb") as f:
            f.write(response.body)
        self.log(f"Saved File ${filename}")
