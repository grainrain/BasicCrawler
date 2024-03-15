import scrapy

from BasicCrawler.items import BasiccrawlerItem


class BasiccrawlerspiderSpider(scrapy.Spider):
    name = "BasicCrawlerSpider"
    allowed_domains = ["zaobao.com"]
    # start_urls = ["https://www.zaobao.com/realtime/china"]

    def start_requests(self):
        urls = [
            'https://www.zaobao.com/realtime/china'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            # yield scrapy.Request(url=url, callback=self.parse, meta={'url': url}, dont_filter=True)

    def parse(self, response):
        print(20 * "-", '热点新闻', 20 * "-")
        hot_news_list = response.xpath("//div[@id='main-container']/div[contains(@class,'float-lg-right')]//a")
        for news in hot_news_list:
            title = news.xpath("./@title").extract_first()
            url = news.xpath("./@href").extract_first()
            url = response.urljoin(url)
            print(title, '/', url)
        pass

        print(20 * "-", '新闻列表', 20 * "-")
        news_list = response.xpath("//div[@id='main-container']/div[contains(@class,'float-lg-left')]//a")
        for news in news_list:
            item = BasiccrawlerItem()
            title = news.xpath("./div[@class='flex-1']/div[1]/text()").extract_first()
            publish_date = news.xpath("./div[@class='flex-1']/div[2]/text()").extract_first()
            url = news.xpath("./@href").extract_first()
            url = response.urljoin(url)
            item['title'] = title
            item['publish_date'] = publish_date
            item['url'] = url
            print(title, '/', publish_date, '/', url)
            yield item
        pass
