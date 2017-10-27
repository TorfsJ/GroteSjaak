from dom.thread import Thread


class Document:
    def __init__(self, doc_id):
        self.threads = []
        self.doc_id = doc_id

    def add_thread(self, thread):
        self.threads.append(thread)
