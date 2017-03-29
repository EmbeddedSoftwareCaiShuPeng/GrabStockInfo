# -*- coding: utf-8 -*-

import os
import traceback
import urllib2
import HTMLParser

import mysql.connector
import logging.config
from ConfigParser import SafeConfigParser


PRO_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
LOG_PATH = os.path.join(PRO_DIR_PATH, "log")
CONF_PATH = os.path.join(PRO_DIR_PATH, "conf")

CONF_LOG = os.path.join(CONF_PATH, "logging.properties")
logging.config.fileConfig(CONF_LOG)
logger = logging.getLogger()

config = SafeConfigParser()
config.read(os.path.join(CONF_PATH, 'sys.properties'))


def download_page(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    html = response.read()
    return html


def save_file(file_path, file_content):
    with open(file_path, 'w+') as dest_file:
        dest_file.write(file_content)


def main():
    try:
        logger.info("==========Script Start=============")
        content = download_page("http://www.baidu.com")
        save_file("test.html", content)
        logger.info("==========Script Finish=============")
    except:
        logger.error("Run script error: %s", traceback.format_exc())


if "__main__" == __name__:
    main()
