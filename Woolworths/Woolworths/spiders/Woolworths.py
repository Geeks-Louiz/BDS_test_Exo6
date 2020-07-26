
import scrapy
from Woolworths.items import WoolworthsItem

class Woolworths(scrapy.Spider):
    name = 'Woolworths'
    allowed_domains = ['woolworths.com']


    data = {
    'excludeUnavailable': 'true',
    'source': 'RR-Best Sellers'}

    def start_requests(self):
        url = 'https://www.woolworths.com.au/apis/ui/products/69418, 714860, 69391, 427069, 305195, 875796, 201688, 208073,305224,576392,82144,576360,636330,365023,669791,479502,305223,612010,586822,305224,479502,35498,154991,54631'
        yield scrapy.Request(url=url,meta=self.data,callback=self.parse)
    def parse(self, response):
        data = response.json()

        for a in data:
         item= WoolworthsItem()
         item['name']=a['Name']
         item['price']= a['Price']
         yield  item

