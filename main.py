# -*- coding: utf-8 -*-

import os
import traceback
import urllib2
import HTMLParser

import logging.config
from ConfigParser import SafeConfigParser

from stock.StockCodeManager import StockCodeManager
from stock.StockInfoCrawler import StockInfoCrawler


PRO_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
LOG_PATH = os.path.join(PRO_DIR_PATH, "log")
CONF_PATH = os.path.join(PRO_DIR_PATH, "conf")

CONF_LOG = os.path.join(CONF_PATH, "logging.properties")
logging.config.fileConfig(CONF_LOG)
logger = logging.getLogger()

config = SafeConfigParser()
config.read(os.path.join(CONF_PATH, 'sys.properties'))


def save_file(file_path, file_content):
    with open(file_path, 'w+') as dest_file:
        dest_file.write(file_content)


def main():
    try:
        logger.info("==========Script Start=============")
        stock_info = StockInfoCrawler('000001')
        basic_info = stock_info.catch_stock_basic_info()
        logger.info(basic_info)
        logger.info("==========Script Finish=============")
    except:
        logger.error("Run script error: %s", traceback.format_exc())


if "__main__" == __name__:
    main()
