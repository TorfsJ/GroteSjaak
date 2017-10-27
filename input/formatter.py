from bs4 import BeautifulSoup

from dom.thread import Thread


class XmlFormatter:
    sequence = 0
    def create_document(self, file):
        document = file

    def convert_to_threads(self):
        thread = Thread()
