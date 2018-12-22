from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["amazon.com"]
    start_urls = [
        "https://www.amazon.com/Mega-Man-11-Nintendo-Switch/dp/B07DDG73GD?ref_=Oct_BSellerC_16227133011_7&pf_rd_p=5e3dd1d2-1cf8-5c78-aff3-187767d76808&pf_rd_s=merchandised-search-6&pf_rd_t=101&pf_rd_i=16227133011&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=2H81RQX4G0XYRYC9N26W&th=1"
    ]

    def parse(self, response):
        parameters = Selector(response).xpath('//*[@id="dp-container"]')
        with open('item.txt', 'w') as f: 
            for parameter in parameters:
                item = StackItem()
                item['title'] = parameter.xpath(
                    '/html/head/meta[@name="title"]/@content').extract()
                f.write('Title:   ' + str(item['title']) + '\n')
                item['sku'] = parameter.xpath(
                    '//*[@id="productDetails_detailBullets_sections1"]//td/text()').extract()[0]
                f.write('SKU:   ' + str(item['sku']).replace('\n', '') + '\n')    
                item['price'] = parameter.xpath(
                    '//*[@id="priceblock_ourprice"]/span[2]/text()').extract()
                f.write('price:   ' + str(item['price']) + '\n')       
                item['images'] = parameter.xpath(
                    '//*[@id="landingImage"]').extract()   
                f.write('images:   ' + str(item['images']) + '\n')       
                item['description'] = parameter.xpath(
                    '/html/head/meta[@name="description"]/@content').extract()
                f.write('description:   ' + str(item['description']) + '\n')     
                item['rating'] = parameter.xpath(
                    '//*[@id="reviewsMedley"]/div/div[1]/div[1]/div/div/div[2]/div/span/span/a/span/text()').extract()  
                f.write('rating:   ' + str(item['rating']) + '\n')                                                       
                yield item
        
             
            
