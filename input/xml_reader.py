from xml.dom import minidom


class XmlReader:
    def __init__(self):
        self._input = ""

    def readfile(self):
        file = minidom.parse("../data/SemEval2016-Task3-CQA-QL-dev-subtaskA.xml")
        threadlist = file.getElementsByTagName('Thread')
        print(len(threadlist))
        return len(threadlist)
