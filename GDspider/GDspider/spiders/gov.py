import scrapy


#title： /html/body/div[@class='con']/div[@class='viewList']/ul/li[1]/span[@class='til']/a
#time： /html/body/div[@class='con']/div[@class='viewList']/ul/li[1]/span[@class='time']
#link； /html/body/div[@class='con']/div[@class='viewList']/ul/li[1]/span[@class='til']/a//@href

class GovSpider(scrapy.Spider):
    name = 'gov'
    allowed_domains = ['www.gd.gov.cn']
    baseURL = "http://www.gd.gov.cn/zwgk/wjk/qbwj/yf/index"
    offset = 1
    end = '.html'
    start_urls = ['http://www.gd.gov.cn/zwgk/wjk/qbwj/yf/index.html']

    def parse(self, response):
        node_list = response.xpath("/html/body/div[@class='con']/div[@class='viewList']/ul/li")

        for node in node_list:
            print(node)