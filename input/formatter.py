from dom.thread import Thread

from dom.question import Question
from dom.forum import Forum
from dom.thread import Thread
from dom.comment import Comment

from bs4 import BeautifulSoup


class XmlFormatter:
    def __init__(self, file_uri):
        self.file_uri = file_uri
        self.forum = Forum()

    @property
    def convert_data(self):
        forum = Forum()
        with open('../data/SemEval2016-Task3-CQA-QL-train-part2-subtaskA.xml', encoding="utf8") as file:
            try:
                xml = file.read()
            finally:
                file.close()
        soup = BeautifulSoup(xml, "lxml")
        for thread in soup.find_all('thread'):
            xml_question = thread.find('relquestion')
            q_id = xml_question["relq_id"]
            question = Question(q_id, xml_question.text)
            thread_obj = Thread(question)
            for thread_comment in thread.find_all('relcomment'):
                c_id = thread_comment["relc_id"]
                c_relevance = thread_comment["relc_relevance2relq"]
                c_text = thread_comment.text
                comment = Comment(c_relevance, c_text, c_id)
                thread_obj.add_comment(comment)
            forum.add_thread(thread_obj)
        return forum