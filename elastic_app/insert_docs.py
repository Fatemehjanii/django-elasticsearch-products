import random
from datetime import datetime
from elasticsearch import Elasticsearch,helpers
from elastic_client import client

index_name = "products"


if not client.indices.exists(index=index_name):
    mapping = {
        "mappings": {
            "properties": {
                "product_id": {"type": "keyword"},
                "category": {"type": "keyword"},
                "color": {"type": "keyword"},
                "size": {"type": "keyword"},
                "price": {"type": "float"},
                "stock": {"type": "boolean"},
                "description": {"type": "text"},
                "insert_time": {"type": "date"}
            }
        }
    }
    client.indices.create(index=index_name, body=mapping)
    print("✅ Index created")
else:
    print("ℹ️ Index already exists")


categories = ["cap", "bag", "shoes", "scarf", "dress"]
colors = ["black", "white", "red", "blue", "beige"]
sizes = ["S", "M", "L", "XL"]
prices = [15.0, 16.0, 100.0, 50.0]
descriptions = ["pretty", "cheap", "high quality", "classic", "lux"]


documents = []

for i in range(1, 101):
    doc = {
        "_index": index_name,
        "_source": {
            "product_id": f"P{i:03d}",
            "category": random.choice(categories),
            "size": random.choice(sizes),
            "color": random.choice(colors),
            "price": random.choice(prices),
            "stock": random.choice([True, False]),
            "description": random.choice(descriptions),
            "insert_time": datetime.now()
        }
    }
    documents.append(doc)


helpers.bulk(client=client, actions=documents)
print("Bulk inserted successfully")
