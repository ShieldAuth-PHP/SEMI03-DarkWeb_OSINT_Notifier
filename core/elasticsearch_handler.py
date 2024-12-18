import os

from elasticsearch import Elasticsearch


def get_es_client():
    return Elasticsearch(
        os.getenv("ELASTICSEARCH_URL"),
        basic_auth=(os.getenv("ELASTIC_USER"), os.getenv("ELASTIC_PASSWORD")),
        ca_certs="/path/to/http_ca.crt"
    )

def insert_data(index, doc_id, data):
    es = get_es_client()
    res = es.index(index=index, id=doc_id, body=data)
    return res