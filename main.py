from helpers.data_convertor import Xml_convertor


class Main:
    def main():
        forum = Xml_convertor.convert_data("dfss")
        forum.make_models()
        for thread in forum.threads:
            querytermen = thread.question.query_model.query_terms
            for comment in thread.comments:
                comment.document_model.prob_document_given_query(querytermen)
        threadzero = forum.threads[0]
        for comment in threadzero.comments:
            print("%s %s %s %s \n" % (threadzero.question.question_id, comment.comment_id,
                  comment.document_model.rank_value, comment.relevance))

    if __name__ == '__main__':
        main()
