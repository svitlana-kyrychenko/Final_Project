CREATE KEYSPACE project WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 3 };
USE project;
DROP TABLE IF EXISTS domains;
CREATE TABLE IF NOT EXISTS domains (
    domain_name text,
    uri text,
    PRIMARY KEY (domain_name, uri));

DROP TABLE IF EXISTS user_pages;
CREATE TABLE IF NOT EXISTS user_pages (
    user_id text,
    page_id text,
    uri text,
    PRIMARY KEY (user_id, page_id));

DROP TABLE IF EXISTS page_ids;
CREATE TABLE IF NOT EXISTS page_ids (
    page_id text,
    uri text,
    PRIMARY KEY (page_id, uri));
