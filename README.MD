```
pip install scrapy==2.11.2  

pip install fake-useragent==1.1.0  

pip install scrapy_fake_useragent==1.4.4  

pip install pipreqs

pipreqs . --encoding=utf8 --force
```

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
