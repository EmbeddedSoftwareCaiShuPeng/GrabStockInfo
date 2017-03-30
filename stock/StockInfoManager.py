# -*- coding: utf-8 -*-


from utils.PageDownloader import PageDownloader


class StockInfoManager():
    """
    This class is for downloading stock's information from wangyi
    """

    STOCK_INFO_URL = 'http://quotes.money.163.com/1%s.html'
    STOCK_NAME_LABEL = '<a href=\'/1%s.html\'>'

    @classmethod
    def get_stock_info(cls, code):
        stock_info = {}
        url = cls.STOCK_INFO_URL % code

        content = PageDownloader.download_page(url)
        stock_info['basic_info'] = cls.get_stock_basic_info(code, content)

        return stock_info


    @classmethod
    def get_stock_basic_info(cls, code, content):
        basic_info = {}

        # get stock name
        basic_info['name'] = content.split(cls.STOCK_NAME_LABEL % code)[1].split('</a>')[0]

        return basic_info
