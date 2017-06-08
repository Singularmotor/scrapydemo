#coding=utf-8
import scrapy
from scrapy.spider import Spider

class demosp(Spider):
    name="demosp"
    allowed_domains=["runoob.com"]
    #allow_domains是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页。
    start_urls=["http://www.runoob.com/git/git-tutorial.html",
                "http://www.runoob.com/python3/python3-tutorial.html"]

    def parse(self,response):
        filename=response.url.split("/")[-2]
        open(filename,'wb').write(response.body)