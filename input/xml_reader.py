from bs4 import BeautifulSoup

class XmlReader:
    def __init__(self, fileUri):
        self._fileUri = fileUri

    def readfile(self):
        file = open("../data/SemEval2016-Task3-CQA-QL-dev-subtaskA.xml")
        return file
