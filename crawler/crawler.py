import scrapy

class ExampleSpider(scrapy.Spider):
    name = "example_spider"
    start_urls = ["https://example.com"]

    def parse(self, response):
        title = response.xpath("//title/text()").get()
        yield {"title": title}

if __name__ == "__main__":
    # For quick testing, you can run scrapy from code:
    from scrapy.crawler import CrawlerProcess
    process = CrawlerProcess()
    process.crawl(ExampleSpider)
    process.start()

