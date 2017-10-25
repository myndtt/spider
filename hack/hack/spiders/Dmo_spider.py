# -*- coding: utf-8 -*-
from scrapy.spider import Spider
import urllib
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class DmozSpider(Spider):
    name="dmoz"
    allowed_domains=["xiaohuar.com"]
    start_urls=[
    ]
    def start_requests(self):
            for i in xrange(39,44):
                url="http://www.xiaohuar.com/list-1-%s.html" % i
                #print url
                #print url
                self.start_urls.append(url)
            for line in self.start_urls:
                yield self.make_requests_from_url(line)
    def parse(self, response):
        name=response.xpath('//*[@id="list_img"]/div/div[1]/div/div[1]/div[1]/a/img/@alt').extract()
        url=response.xpath('//*[@id="list_img"]/div/div[1]/div/div[1]/div[1]/a/img/@src').extract()
        for i in xrange(len(name)):
            print name[i]
            file_name=str(name[i])+".jpg"
            absolutesrc="http://www.xiaohuar.com"+str(url[i])
            print absolutesrc
            file_path=os.path.join(u"d:\\pic",file_name)
            urllib.urlretrieve(absolutesrc,file_path)

