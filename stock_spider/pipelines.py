# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class StockSpiderPipeline(object):
  def process_item(self, item, spider):
    print item["region"] + "\t" + item["name"] + "\t" + item["code"]
