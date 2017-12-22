from model.collection_model import CollectionModel


class Forum:
    def __init__(self):
        self.threads = []
        self.collection_model = 0

    def add_thread(self, thread):
        self.threads.append(thread)

    def make_models(self):
        self.collection_model = CollectionModel(self)
        for thread in self.threads:
            thread.make_models()
