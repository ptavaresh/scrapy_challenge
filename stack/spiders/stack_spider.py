from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        #"https://www.amazon.com.mx/Funko-Figure-Holiday-Darth-Multicolor/dp/B07DFDXV4W/ref=sr_1_2?s=toys&rps=1&ie=UTF8&qid=1545349524&sr=1-2"
        "https://www.amazon.com/Mega-Man-11-Nintendo-Switch/dp/B07DDG73GD?ref_=Oct_BSellerC_16227133011_7&pf_rd_p=5e3dd1d2-1cf8-5c78-aff3-187767d76808&pf_rd_s=merchandised-search-6&pf_rd_t=101&pf_rd_i=16227133011&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=2H81RQX4G0XYRYC9N26W&th=1"
        #"http://stackoverflow.com/questions?pagesize=50&sort=newest",
        #"https://dbader.org/blog/",
    ]

    def parse(self, response):
        parameters = Selector(response).xpath('//*[@id="dp-container"]')#('//header/h1')
        i=0
        for parameter in parameters:
            item = StackItem()
            item['title'] = parameter.xpath(
                '/html/head/meta[@name="title"]/@content').extract()#'//h1/a/text()').extract()[i]
            item['sku'] = parameter.xpath(
                '//*[@id="productDetails_detailBullets_sections1"]//td/text()').extract()[0]
            item['price'] = parameter.xpath(
                '//*[@id="priceblock_ourprice"]/span[2]/text()').extract()
            item['images'] = parameter.xpath(
                '//*[@id="landingImage"]').extract()   
            item['description'] = parameter.xpath(
                '/html/head/meta[@name="description"]/@content').extract()  
            item['rating'] = parameter.xpath(
                '//*[@id="reviewsMedley"]/div/div[1]/div[1]/div/div/div[2]/div/span/span/a/span/text()').extract()                                                      
            i = i +1
            print(item['sku'])
            yield item
            
