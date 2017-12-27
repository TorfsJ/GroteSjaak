from helpers.data_convertor import Xml_convertor
from helpers.data_writer import DataWriter

class Main:
    def main():
        file_uri = "SemEval2016-Task3-CQA-QL-train-part2-subtaskA.xml"
        forum = Xml_convertor.convert_data(file_uri)
        forum.make_models()
        for thread in forum.threads:
            thread.calculate_ranking(forum.collection_model)
        DataWriter.write_forum_to_file(forum, file_uri)

    if __name__ == '__main__':
        main()
