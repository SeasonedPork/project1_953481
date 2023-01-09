import numpy as np

from solar import *

from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")
#
class Indexer:
    b = input("please enter index name : ")
    def __init__(self):
        self.crawled_folder = Path(os.path.abspath('resource')).parent / './crawled/'
        with open(self.crawled_folder / 'url_list.pickle', 'rb') as f:
            self.file_mapper = pickle.load(f)
        self.es_client = Elasticsearch('http://localhost:9200')

    def run_indexer(self):
        self.es_client.options(ignore_status=400).indices.create(index='simple')
        self.es_client.options(ignore_status=[400, 404]).indices.delete(index='simple')

        for file in os.listdir(self.crawled_folder):
            if file.endswith(".txt"):
                j = json.load(open(os.path.join(self.crawled_folder, file),encoding="utf-8"))
                j['id'] = j['url']
                print("indexing....")
                self.es_client.index(index=Indexer.b, document=j)

    def user_input_index(self):
        a = Indexer.b
        self.es_client.options(ignore_status=400).indices.create(index=a)
        self.es_client.options(ignore_status=[400, 404]).indices.delete(index=a)

        for file in os.listdir(self.crawled_folder):
            if file.endswith(".txt"):
                j = json.load(open(os.path.join(self.crawled_folder, file), encoding="utf-8"))
                j['id'] = j['url']
                print("indexing....")
                self.es_client.index(index=input("please enter name for index:"), document=j)


# def user_create_index(input_user):




if __name__ == '__main__':
    s = Indexer()
    s.run_indexer()
    query = {"match": {"text":input("please enter query keyword :")}}
    # results = s.es_client.search(index=input("this is creating index please enter text:"), query=query)
    # query = {'bool': {'must': [{'match': {'text': 'exam'}}]}}
    results = s.es_client.search(index=s.b, query=query)
    print("Got %d Hits:" % results['hits']['total']['value'])

    # for hit in results['hits']['hits']:
    #     print("The title is '{0} ({1})'.".format(hit["_source"]['title'], hit["_source"]['url']))
    # query = {'bool': {'must': [{'match': {'text': 'examination'}}]}}
    # query = {"regexp": {"text": ".*vision.*"}}
    # query = {"match": {"text": "vision"}}

