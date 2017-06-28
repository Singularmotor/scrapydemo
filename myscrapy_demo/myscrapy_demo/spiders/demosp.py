#coding=utf-8
import scrapy
from scrapy.spider import Spider

class demosp(Spider):
    name="demosp"
    allowed_domains=["jb51.net"]
    #allow_domains是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页。
    start_urls=["http://www.jb51.net/article/92516.htm"]

    def parse(self,response):
        filename=response.url.split("/")[-2]
        open(filename,'wb').write(response.body)