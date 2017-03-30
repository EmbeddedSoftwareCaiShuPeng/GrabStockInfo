# -*- coding: utf-8 -*-


from utils.PageDownloader import PageDownloader


class StockCodeManager():
    """
    This class is for managing all stock code
    """

    STOCK_LIST_URL = 'http://quote.eastmoney.com/stocklist.html#sh'

    @classmethod
    def get_all_stock_code_list(cls):
        code_list = []
        content = PageDownloader.download_page(cls.STOCK_LIST_URL)

        sz_code_list = cls.get_sz_stock_code_list(content)
        sh_code_list = cls.get_sh_stock_code_list(content)

        code_list.extend(sz_code_list)
        code_list.extend(sh_code_list)
        return code_list

    @classmethod
    def get_sz_stock_code_list(cls, content):
        content_list = content.split("a name=\"sh\"")[1].split("/ul")[0].split("(")
        code_list = []

        for item in content_list:
            code = item.split(")")[0]
            code_list.append(code)

        return code_list

    @classmethod
    def get_sh_stock_code_list(cls, content):
        content_list = content.split("a name=\"sz\"")[1].split("/ul")[0].split("(")
        code_list = []

        for item in content_list:
            code = item.split(")")[0]
            code_list.append(code)

        return code_list
