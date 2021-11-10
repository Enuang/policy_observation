# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from items import *

class GdspiderPipeline(object):
    def __init__(self):
        self.f = open("GDgovment.json","w")
        self.f = open("title.json", "w")
        self.file_detail = open("detail.json", "w")

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False)

        if isinstance(item, GdspiderItem):
            self.f.write(content + ',\n')

        if isinstance(item, DetailsItem):
            self.file_detail.write(content + ',\n')

        return item

    def close_spider(self, spider):
        self.f.close()
        self.file_detail.close()