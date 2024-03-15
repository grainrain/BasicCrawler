pip install scrapy
pip install scrapy_fake_useragent


`scrapy crawl BasicCrawlerSpider`

```commandline
scrapy crawl BasicCrawlerSpider -o basic.json 

scrapy crawl BasicCrawlerSpider -o basic.csv   -s CLOSESPIDER_ITEMCOUNT=90

scrapy crawl BasicCrawlerSpider -o basic.xml
```


```commandline
scrapy crawl BasicCrawlerSpider -s FEED_URI='d:\\basic.csv' -s FEED_FORMAT=csv 

scrapy crawl BasicCrawlerSpider -s FEED_URI='d:\\basic.json' -s FEED_FORMAT=json
```
