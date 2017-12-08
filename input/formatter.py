from dom.thread import Thread

from bs4 import BeautifulSoup


class XmlFormatter:
    def __init__(self, file_uri):
        self.file_uri = file_uri

    def convert_data(self):
        file = open("../data/CD.xml", "r")
        xml = file.read()
        soup = BeautifulSoup(xml, "lxml")
        for thread in soup.find_all('Thread'):
            question = thread.find('RelQuestion')
            print(question.text)

    def readfile(self):
        # file = open("../data/SemEval2016-Task3-CQA-QL-train-part1-subtaskA.xml")
        # xml = file.read(file)
        with open("../data/SemEval2016-Task3-CQA-QL-train-part1-subtaskA.xml") as f:
            xml =  f.read()
            return f