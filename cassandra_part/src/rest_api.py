from flask import Flask, request, jsonify
from batches_from_kafka import CassandraClient
import json

app = Flask(__name__)
host = 'cassandra-server'
port = 9042
keyspace = 'project'


@app.get("/all_domains")
def get_all_domains():
    return json.dumps(client.select_domains(), indent=4, sort_keys=True, default=str)


@app.get("/user_pages&user_id=<user_id>")
def user_page(user_id):
    return json.dumps(client.select_user_page(user_id), indent=4, sort_keys=True, default=str)


@app.get("/domain_articles&domain=<domain>")
def articles_by_domain(domain):
    return json.dumps(client.select_articles_by_domain(domain), indent=4, sort_keys=True, default=str)


@app.get("/page&page_id=<page_id>")
def page(page_id):
    return json.dumps(client.select_page_by_id(page_id), indent=4, sort_keys=True, default=str)


if __name__ == "__main__":
    client = CassandraClient(host='cassandra-server', port=port, keyspace='project')
    client.connect()
    app.run(host="0.0.0.0", port=8080)
