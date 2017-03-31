# -*- coding: utf-8 -*-


from utils.PageDownloader import PageDownloader


class StockInfo:
    """
    This class is for downloading stock's information from wangyi
    """

    STOCK_INFO_URL = 'http://quotes.money.163.com/1%s.html'
    STOCK_NAME_LABEL = '<a href=\'/1%s.html\'>'

    __stock_code = ''

    def __init__(self, stock_code):
        self.__stock_code = stock_code

    def refresh_info(self):
        isExist = Flase

        if not isExist:
            print 'Continue'

        stock_info = self.catch_stock_info()

    def catch_stock_info(self):
        stock_info = {}

        stock_info['basic_info'] = self.catch_stock_basic_info()
        stock_info['relevant_info'] = self.catch_stock_basic_info()
        stock_info['financial_data'] = self.catch_stock_financial_data()

        return stock_info

    def catch_stock_basic_info(self):
        basic_info = {}

        url = self.STOCK_INFO_URL % self.__stock_code
        content = PageDownloader.download_page(url)

        # get stock name
        basic_info['name'] = content.split(self.STOCK_NAME_LABEL % self.__stock_code)[1].split('</a>')[0]

        return basic_info

    def catch_stock_relevant_info(self):
        relevant_info = {}

        return relevant_info

    def catch_stock_financial_data(self):
        financial_data = {}

        balance_sheet_list = self.catch_balance_sheet_list()
        income_statement_list = self.catch_income_statement_list()
        cash_flow_statement_list = self.catch_cash_flow_statement_list()

        for balance_sheet in balance_sheet_list:
            financial_data[balance_sheet['date']]['balance_sheet'] = balance_sheet

        for income_statement in income_statement_list:
            financial_data[income_statement['date']]['income_statement'] = income_statement

        for cash_flow_statement in cash_flow_statement_list:
            financial_data[cash_flow_statement['date']]['cash_flow_statement'] = cash_flow_statement

        return financial_data

    def catch_balance_sheet_list(self):
        balance_sheet_list = []

        return balance_sheet_list

    def catch_income_statement_list(self):
        income_statement_list = []

        return income_statement_list

    def catch_cash_flow_statement_list(self):
        cash_flow_statement_list = []

        return cash_flow_statement_list
