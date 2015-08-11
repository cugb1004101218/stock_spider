# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import scrapy
from stock_spider.items import Stock

class CrawlStockSpider(scrapy.Spider):
  name = "crawl_stock"
  allowed_domains = ["quote.stockstar.com"]
  start_urls = (
    'http://quote.stockstar.com/stock/small.shtml',
  )

  def parse(self, response):
    urls = {
      '沪市A股': 'http://quote.stockstar.com/stock/sha_3_1_',
      '沪市B股': 'http://quote.stockstar.com/stock/shb_3_1_',
      '深市A股': 'http://quote.stockstar.com/stock/sza_3_1_',
      '深市B股': 'http://quote.stockstar.com/stock/szb_3_1_',
      '中小板': 'http://quote.stockstar.com/stock/small_3_1_',
      '创业板': 'http://quote.stockstar.com/stock/gem_3_1_',
      'A股市场': 'http://quote.stockstar.com/stock/ranklist_a_3_1_',
      'B股市场': 'http://quote.stockstar.com/stock/ranklist_b_3_1_',
      '沪市A+B股': 'http://quote.stockstar.com/stock/ab_sh.shtml',
      '深市A+B股': 'http://quote.stockstar.com/stock/ab_sz.shtml',
      '新股': 'http://quote.stockstar.com/stock/ipo.shtml',
      '沪港通': 'http://quote.stockstar.com/stock/blockperformance_0_400129614_0_0_',
      '三板': 'http://quote.stockstar.com/stockmarket/threeboard_5_1_',
    }
    for region in urls:
      url = urls[region]
      # 列表
      if url[-1] == '_':
        for i in range(1, 200):
          yield scrapy.http.Request(url=url + str(i) + '.html', callback=lambda response, region=region: self.CrawlStockList(response, region))
      else:  # 只有一页的
        yield scrapy.http.Request(url=url, callback=lambda response, region=region: self.CrawlStockList(response, region))


  def CrawlStockList(self, response, region):
    stock_list = response.selector.xpath('/html/body/div[@class="w"]/div[@class="sideRight"]//table/tbody/tr')
    if len(stock_list) == 0:
      return
    for stock in stock_list:
      try:
        code = stock.xpath('td//a/text()').extract()[0]
        name = stock.xpath('td//a/text()').extract()[1]
        if code == None or name == None:
          continue
        yield Stock({"region": region, "code": code, "name": name})
      except:
        pass
