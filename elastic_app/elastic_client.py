from elasticsearch import Elasticsearch


client = Elasticsearch("http://localhost:9200")

if client.ping():
    print("Ping is working")
else:
    print("Ping is not working")