import scrapy
from scrapy_splash import SplashRequest


class BasiccrawlerspiderSpider(scrapy.Spider):
    name = "BasicCrawlerSpider"
    allowed_domains = ["zaobao.com"]
    # start_urls = ["https://www.zaobao.com/realtime/china"]

    def start_requests(self):
        urls = [
            'https://newiic.jaas.ac.cn/xww/tzgg/index.html'
        ]
        for url in urls:
            yield SplashRequest(url=url,args={'wait': 5,  'timeout': 90}, dont_filter=True)

    def parse(self, response):
        print(20 * "-", '新闻列表', 20 * "-")
        news_list = response.xpath("//*[@id='当前栏目list']/div[1]/ul/li")
        for news in news_list:
            title = news.xpath("./label[1]/a/@title").extract_first()
            publish_date = news.xpath("./label[2]/text()").extract_first()
            url = news.xpath("./label[1]/a/@href").extract_first()
            url = response.urljoin(url)
            print(title, '/', publish_date, '/', url)
        pass
