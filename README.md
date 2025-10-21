# 🧠 Elasticsearch Learning Lab
**by Fatemeh Jani | Computer Engineer & DevOps Learner & Backend Developer**

![Elastic Logo](https://upload.wikimedia.org/wikipedia/commons/0/05/Elastic_logo.svg)

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

## 💡 Example Queries

| # | Query Type | Example | Description |
|---|-------------|----------|-------------|
| 1 | match_all | – | Returns all documents |
| 2 | match | description="cheap" | Full-text search |
| 3 | range | price 0–20 | Filter by price range |
| 4 | fuzzy | description="clasic" | Finds "classic" with typo |
| 5 | wildcard | product_id="P0*" | IDs starting with “P0” |

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

## 👩‍💻 Author
**Fatemeh Jani**  
Computer Engineer | DevOps & AI Enthusiast  
Member of **Venomuse Rose Team** 🌸  
Focus: Automation • Search Systems • Data Engineering  

🔗 [GitHub Profile](https://github.com/Fatemehjanii)

---

## ⭐ Support
If you find this project useful, please give it a ⭐ on GitHub —  
it motivates me to share more open-source learning projects!

> 💬 “Search is not just finding — it’s understanding data.” — *Fatemeh Jani*
