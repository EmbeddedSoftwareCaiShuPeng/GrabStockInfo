# -*- coding: utf-8 -*-

import os
import traceback
import urllib2
import HTMLParser

import logging.config
from ConfigParser import SafeConfigParser


class PageDownloader():
    """
    This class is for downloading page from Internet
    """

    @classmethod
    def download_page(cls, url):
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        html_content = response.read()
        try:
            html_content.decode('utf-8')
        except:
            print ''
        return html_content
