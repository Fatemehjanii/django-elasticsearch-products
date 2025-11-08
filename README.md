# 🧠 Elasticsearch Learning Lab
**by Fatemeh Jani | Computer Engineer & DevOps Learner & Backend Developer**

[![Elasticsearch Logo](https://upload.wikimedia.org/wikipedia/commons/f/f4/Elasticsearch_logo.svg)](https://www.elastic.co/)


---

## 🌍 Overview
This repository is part of my **Elasticsearch learning journey** — focusing on mastering **data indexing, searching, and scalability** concepts.

It includes **Python scripts**, **real-world queries**, and **hands-on experiments** with a local Elasticsearch cluster integrated into a Django project.

> 📘 **Goal:** Gain solid, hands-on experience with Elasticsearch for DevOps, backend, and data engineering applications.

---

## 🧩 Topics Covered

| # | Concept | Description |
|---|----------|-------------|
| 1 | Structured vs Unstructured Data | Understanding data organization and schema differences |
| 2 | Cluster | What an Elasticsearch cluster is and how it manages nodes |
| 3 | Scalability | Vertical vs Horizontal scaling concepts |
| 4 | Shards & Replicas | Internal data distribution and fault tolerance |
| 5 | Index & Templates | Creating indices, managing templates, and understanding index health |
| 6 | Documents | Creating and inserting 100 structured documents using Python |
| 7 | Elasticsearch DSL | Query language (match, filter, range, fuzzy, wildcard, etc.) |
| 8 | Aggregations | 5 aggregation types and their practical use cases |
| 9 | Reindex & Clone | Difference between reindexing and cloning |
| 10 | KQL & Kibana | Querying data using Kibana dashboards |

---

## ⚙️ Project Structure

```
elasticsearch-lab/
│
├── elastic_app/                 # Django app for Elasticsearch integration
│   ├── elastic_client.py        # Elasticsearch connection setup
│   ├── insert_docs.py           # Script to insert 100 random documents
│   ├── views.py                 # Django views for running queries
│   └── models.py                # Django models (if ORM used)
│
├── elasticsearch_lab/           # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/                   # HTML templates (optional)
├── db.sqlite3                   # Django local DB
├── manage.py                    # Django management script
├── requirements.txt             # Dependencies
├── README.md                    # Documentation
└── LICENSE                      # License file (e.g., MIT)
```

---

## 🚀 How to Run

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Fatemehjanii/django-elasticsearch-products.git
cd django-elasticsearch-products
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Local Elasticsearch
**Option A – via Docker:**
```bash
docker run -d --name elasticsearch -p 9200:9200 -e "discovery.type=single-node" elasticsearch:8.14.0
```

**Option B – via Local Installation:**
Run the Elasticsearch service from your system installation.

---

### 4️⃣ Insert Sample Documents
```bash
python elastic_app/insert_docs.py
```

---

### 5️⃣ Run the Django Project
```bash
python manage.py runserver
```

---

# 💡 Example Elasticsearch Queries

| # | Query Type | Example | Description |
|---|------------|---------|-------------|
| 1 | match_all | – | Returns all documents |
| 2 | match | description="cheap" | Full-text search for "cheap" |
| 3 | match | description="classic" | Full-text search for "classic" |
| 4 | match | description="lux" | Full-text search for "lux" |
| 5 | term | stock=true | Only available products |
| 6 | term | stock=false | Only unavailable products |
| 7 | term | category="cap" | Products in the "cap" category |
| 8 | term | category="bag" | Products in the "bag" category |
| 9 | term | category="shoes" | Products in the "shoes" category |
| 10 | term | category="scarf" | Products in the "scarf" category |
| 11 | term | category="dress" | Products in the "dress" category |
| 12 | range | price 0–20 | Filter by price range 0–20 |
| 13 | range | price 20–50 | Filter by price range 20–50 |
| 14 | range | price 50–100 | Filter by price range 50–100 |
| 15 | range | rating 1–2 | Filter by rating 1–2 |
| 16 | range | rating 3–4 | Filter by rating 3–4 |
| 17 | fuzzy | description="chep" | Finds "cheap" with typo |
| 18 | fuzzy | description="clasic" | Finds "classic" with typo |
| 19 | fuzzy | category="capA" | Finds category "capA" with typo |
| 20 | wildcard | product_id="P0*" | All product IDs starting with "P0" |
| 21 | match | description="high quality" | Full-text search for "high quality" |
| 22 | match | description="pretty" | Full-text search for "pretty" |
| 23 | bool must | stock=true + category="bag" | Available products in "bag" category |
| 24 | bool must | stock=true + category="shoes" | Available products in "shoes" category |
| 25 | bool must | stock=true + price<50 | Available products under 50 |
| 26 | bool must + range | stock=true + price 20–50 | Available products in price range 20–50 |
| 27 | bool should | color="red" OR color="blue" | Preferably red or blue |
| 28 | bool should | tags="sale" OR tags="new" | Preferably products on sale or new |
| 29 | bool must_not | category="cap" | Exclude caps |
| 30 | bool must_not | brand="BrandC" | Exclude BrandC |
| 31 | bool must + should | stock=true + (color="red" OR color="blue") | Combination of Must and Should |
| 32 | prefix | color="bl" | All colors starting with "bl" |
| 33 | prefix | product_id="P0" | All product IDs starting with "P0" |
| 34 | aggregation | group by category | Count of products per category |
| 35 | aggregation | avg price by category | Average price per category |
| 36 | aggregation | max price by category | Maximum price per category |
| 37 | aggregation | min price by category | Minimum price per category |
| 38 | aggregation | count by size | Count of products per size |
| 39 | script | price - discount <50 | Products with price after discount <50 |
| 40 | script | rating * 2 | Compute double rating |
| 41 | query_string | "cheap OR lux" | Combined text search |
| 42 | query_string | "category:Category*" | Wildcard search on category |
| 43 | match | description="exclusive" | Search for "exclusive" |
| 44 | match | description="limited" | Search for "limited" |
| 45 | fuzzy | description="exclsuive" | Fuzzy for "exclusive" |
| 46 | fuzzy | description="limted" | Fuzzy for "limited" |
| 47 | wildcard | tags="new*" | Wildcard for tags starting with "new" |
| 48 | wildcard | tags="sale*" | Wildcard for tags starting with "sale" |
| 49 | range | insert_time >= "2025-01-01" | From Jan 1, 2025 |
| 50 | range | insert_time <= "2025-06-01" | Before June 1, 2025 |
| 51 | bool must + filter | stock=true + price<50 | Available products under 50 |
| 52 | bool must + should + filter | stock=true + (color="red" OR color="blue") + price<50 | Combination of Must, Should, and Filter |
| 53 | bool must_not + filter | category!="dress" + price>20 | Exclude dresses and price >20 |
| 54 | aggregation + filter | avg price by category + stock=true | Average price of available products per category |
| 55 | aggregation + range | count by category + price 20–50 | Count per category within price range 20–50 |
| 56 | bool must + script | stock=true + price-discount<50 | Available products with discounted price <50 |
| 57 | query_string + fuzzy | "chep OR clasic" | Combined fuzzy and query_string |
| 58 | match + prefix | description="lux" + color="bl" | "lux" products with color starting "bl" |
| 59 | bool should + wildcard | color="red" OR product_id="p00*" | Should + wildcard |
| 60 | bool must + must_not | stock=true + category!="bag" | Available products excluding bags |
| 61 | range + aggregation | price 20–50 + count by size | Count of each size in price range 20–50 |
| 62 | range + script | price>50 + price-discount>40 | Price range and script calculation |
| 63 | fuzzy + must | description="chep" + stock=true | Fuzzy and available products |
| 64 | fuzzy + should | description="clasic" + color="red" OR color="blue" | Fuzzy and preferred color |
| 65 | wildcard + must | product_id="P0*" + stock=true | Wildcard and available products |
| 66 | wildcard + filter | description="classic*" + price<50 | Wildcard and price filter |
| 67 | query_string + must | "cheap AND size:M" + stock=true | Combined query_string and Must |
| 68 | query_string + filter | "lux OR classic" + price<50 | Combined query_string and filter |
| 69 | match_all + aggregation | all documents + count by category | All documents and count |
| 70 | match_all + script | all documents + price-discount | All documents and price script |
| 71 | bool must + range | stock=true + rating 3–5 | Available products with rating 3–5 |
| 72 | bool should + range | color="red" OR color="blue" + price<50 | Preferred color and price range |
| 73 | bool must_not + fuzzy | category!="dress" + description="clasic" | Exclude dresses and fuzzy search |
| 74 | aggregation + range | avg price by category + price 20–50 | Average price per category in range |
| 75 | aggregation + filter + script | avg(price-discount) by category + stock=true | Avg price after discount for available products |
| 76 | bool must + query_string | stock=true + "cheap OR lux" | Must + query_string |
| 77 | bool should + query_string | color="red" OR color="blue" + "cheap OR lux" | Should + query_string |
| 78 | prefix + fuzzy | color="bl" + description="clasic" | Prefix + fuzzy |
| 79 | wildcard + fuzzy | product_id="P0*" + description="chep" | Wildcard + fuzzy |
| 80 | script + aggregation | price-discount <50 + avg price by category | Script + aggregation |
| 81 | bool must + should + filter + range | stock=true + (color="red" OR color="blue") + price<50 + rating>3 | Complex combination Must, Should, Filter, Range |
| 82 | bool must + script + aggregation | stock=true + price-discount<50 + avg price by size | Must + script + aggregation |
| 83 | bool must_not + fuzzy + range | category!="cap" + description="clasic" + price 20–50 | Exclude category + fuzzy + range |
| 84 | bool must + wildcard + query_string | stock=true + product_id="P0*" + "cheap OR lux" | Must + wildcard + query_string |
| 85 | aggregation + script + filter | avg(price-discount) by category + stock=true | Aggregation + script + filter |
| 86 | bool must + prefix + fuzzy | stock=true + color="bl" + description="clasic" | Must + prefix + fuzzy |
| 87 | bool should + range + wildcard | – | Should + range + wildcard |
| 88 | query_string + script + aggregation | "cheap OR lux" + price-discount <50 + avg by category | query_string + script + aggregation |
| 89 | bool must + aggregation + range | stock=true + count by category + price 20–50 | Must + aggregation + range |
| 90 | match + fuzzy + range | description="clasic" + stock=true + price>20 | Match + fuzzy + range |
| 91 | bool must + should + script + aggregation | stock=true + (color="red" OR color="blue") + price-discount<50 + avg by category | Full combined query |
| 92 | bool must_not + wildcard + fuzzy | category!="bag" + product_id="P0*" + description="chep" | Exclude category + wildcard + fuzzy |
| 93 | prefix + range + aggregation | color="bl" + price<20 + avg by size | Prefix + range + aggregation |
| 94 | fuzzy + range + script | description="clasic" + price<20 + price-discount<40 | Fuzzy + range + script |
| 95 | query_string + must + filter | "cheap AND brand:BrandA" + stock=true + price<50 | Query_string + must + filter |
| 96 | wildcard + aggregation + script | product_id="P0*" + avg price by category + price-discount<50 | Wildcard + aggregation + script |
| 97 | bool must + query_string + fuzzy | stock=true + "lux OR classic" + description="clasic" | Must + query_string + fuzzy |
| 98 | bool should + script + aggregation | color="red" OR color="blue" + price-discount<50 + avg price by category | Should + script + aggregation |
| 99 | match_all + aggregation + script + range | all documents + avg price by category + price-discount<50 + rating>3 | Match_all + aggregation + script + range |
| 100 | bool must + should + filter + range + script + aggregation + query_string | Combination of all concepts above | Full complex query |


---

## 🧠 Advanced Goals
- Write 100+ search queries from simple to complex combinations  
- Build a Kibana dashboard for visualizing search results  
- Add a `timestamp` field for time-based analytics  
- Compare performance of match vs term queries  

---

## 🛠️ Tools & Technologies
- Python 🐍  
- Django 🌐  
- Elasticsearch 🔍  
- Kibana 📊  
- Docker 🐳  

---


## ⭐ Support
If you find this project useful, please give it a ⭐ on GitHub —  
it motivates me to share more open-source learning projects!

> 💬 “Search is not just finding — it’s understanding data.” — *Fatemeh Jani*
