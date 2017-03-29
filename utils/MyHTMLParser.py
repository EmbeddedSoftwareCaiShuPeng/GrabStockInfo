from HTMLParser import HTMLParser


def _attr(attr_list, attr_name):
    for attr in attr_list:
        if attr[0] == attr_name:
            return attr[1]
    return None


def handle_data(self, data):
    if self.lasttag == 'p':
        print("Encountered p data  :", data)


class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = False

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.flag = True

    def handle_endtag(self, tag):
        return

    def handle_data(self, data):
        if self.flag:
            print "Encountered p data  :", data
        self.flag = False


parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1><img src = "" />'
            '<!-- comment --></body></html>')