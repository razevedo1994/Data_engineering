import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Method for loading data into staging tables.

    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Method for inserting data into dimensional tables.

    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Method to connect to the database and perform the load and insert functions.

    """
    config = configparser.ConfigParser()
    config.read_file(open("dwh.cfg"))

    conn = psycopg2.connect(
        "host={} dbname={} user={} password={} port={}".format(
            config.get("DWH", "DWH_HOST"),
            config.get("DWH", "DWH_DB"),
            config.get("DWH", "DWH_DB_USER"),
            config.get("DWH", "DWH_DB_PASSWORD"),
            config.get("DWH", "DWH_PORT"),
        )
    )
    cur = conn.cursor()

    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
