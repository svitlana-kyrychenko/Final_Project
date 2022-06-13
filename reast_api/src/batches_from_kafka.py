from json import loads
from kafka import KafkaConsumer
from datetime import datetime

consumer = KafkaConsumer('wiki-data',
                         bootstrap_servers=['kafka-server:9092'],
                         api_version=(2, 0, 2),
                         value_deserializer=lambda x:
                         loads(x.decode('ascii')))


class CassandraClient:
    def __init__(self, host, port, keyspace):
        self.host = host
        self.port = port
        self.keyspace = keyspace
        self.session = None
        self.row = 0

    def connect(self):
        from cassandra.cluster import Cluster
        cluster = Cluster([self.host], port=self.port)
        self.session = cluster.connect(self.keyspace)

    def execute(self, query):
        return self.session.execute(query)

    def close(self):
        self.session.shutdown()

    def select_domains(self):
        query = f"SELECT DISTINCT domain_name from domains;"
        return list([x[0] for x in self.execute(query)])

    def select_user_page(self, user_id):
        query = f"SELECT uri from user_pages WHERE user_id = '{user_id}';"
        return list(self.execute(query))

    def select_articles_by_domain(self, domain):
        query = f"SELECT COUNT(*) from domains WHERE domain_name = '{domain}';"
        return list(self.execute(query))

    def select_page_by_id(self, page_id):
        query = f"SELECT * from page_ids WHERE page_id = '{page_id}';"
        return list(self.execute(query))

    def insert_domains(self, message):
        domain = message["domain"]
        uri = message["uri"]
        qr = f"INSERT INTO domains (domain_name, uri) VALUES ('{domain}','{uri}')"
        self.execute(qr)

    def insert_user_page(self, message):
        user_id = message["user_id"]
        uri = message["uri"]
        page_id = message["page_id"]
        qr = f"INSERT INTO user_pages (user_id, page_id, uri) VALUES ('{user_id}', '{page_id}', '{uri}')"
        self.execute(qr)

    def insert_page_ids(self, message):
        page_id = message["page_id"]
        uri = message["uri"]
        qr = f"INSERT INTO page_ids (page_id, uri) VALUES ('{page_id}', '{uri}')"
        self.execute(qr)

    def update_all_tables(self, message):
        self.insert_domains(message)
        self.insert_user_page(message)
        self.insert_page_ids(message)


def extract_data(line):
    from ast import literal_eval
    dict_line = literal_eval(line)
    domain = dict_line['meta']['domain']
    uri = dict_line['meta']['uri']
    try:
        user_id = dict_line['performer']['user_id']
    except KeyError:
        user_id = '0'
    page_id = dict_line['page_id']
    page_title = dict_line['page_title'].replace("'", "")
    return {'domain': domain, 'uri': uri, 'user_id': user_id, 'page_id': page_id,
            'page_title': page_title,}


def main():
    client = CassandraClient(host='cassandra-server', port=9042, keyspace='project')
    client.connect()
    for message in consumer:
        message = message.value
        message = extract_data(str(loads(message[5:])))
        client.update_all_tables(message)


if __name__ == '__main__':
    main()
