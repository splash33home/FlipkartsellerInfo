# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class SellerdataSpider(scrapy.Spider):
    name = 'sellerdata'
    allowed_domains = ['www.flipkart.com']
    # start_urls=['https://www.flipkart.com/sellers?pid=MOBFV5FPCJC9ZKRB&otracker=nmenu_sub_Electronics_0_Mi&fetchId=9e25dbf6-43f7-469a-8a29-7395492579c6.MOBFV5FPCJC9ZKRB']

    script =  '''

            function main(splash, args)
            splash.private_mode_enabled = false
            assert(splash:go(args.url))
            assert(splash:wait(0.5))
            sellerBox = assert(splash:select_all("._2Y3EWJ"))
            assert(splash:wait(0.5))
            splash:set_viewport_full()
            return {
            html = splash:html(),
    
            }
            end
 

   ''' 





    def start_requests(self):
         url="https://www.flipkart.com/sellers?pid=MOBFV5FPCJC9ZKRB&otracker=nmenu_sub_Electronics_0_Mi&fetchId=9e25dbf6-43f7-469a-8a29-7395492579c6.MOBFV5FPCJC9ZKRB"
         yield SplashRequest(url,callback=self.parse,endpoint="execute",args={'lua_source':self.script})


    def parse(self,response):

        for product in response.xpath("//div[@class='_2Y3EWJ']"):
            yield{
                'seller_name' :product.xpath(".//div[@class='isp3v_ col-3-12']/div[@class='_3enH42']/span/text()").extract(),
                'rating' :product.xpath(".//div[@class='isp3v_ col-3-12']/div[@class='_3LWZlK _2GCNvL']/text()").extract(),
                'price'  :product.xpath(".//div/div[@class='_3J2v2E']/div[@class='_dqAAI']/div[@class='_25b18c']/div[@class='_30jeq3']/text()").extract()
            }
        
        #  for product in response.xpath("//div[@class='_3enH42']"):
        #      yield{
        #          'title' : product.xpath(".//span/text()").get(),
        #          'rating' : product.xpath("//div[@class='_3LWZlK _2GCNvL']/text()").get(),
        #          'price' : product.xpath("//div[@class='_30jeq3']/text()").get()
        #           }
    # //div[@class='_2Y3EWJ']/div[@class="isp3v_ col-3-12"]/div[@class='_3enH42']/span
    # //div[@class='_2Y3EWJ']/div/div[@class='_3J2v2E']/div[@class='_dqAAI']/div[@class='_25b18c']/div[@class='_30jeq3']/text()
    # //div[@class='_3J2v2E']/div[@class='_dqAAI']/div[@class='_25b18c']/div[@class='_30jeq3']/text()