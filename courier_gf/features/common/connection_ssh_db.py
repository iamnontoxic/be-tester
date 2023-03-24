from typing import Callable
import psycopg2
import sshtunnel
import psycopg2.extras


def connect_ssh_db_admin(callback: Callable, response, *args):
    with sshtunnel.open_tunnel(('v1.gftech.ru', 22115),
                               ssh_username='services-access',
                               remote_bind_address=('db-master-admin-review.growfood.pro', 5432),
                               ssh_pkey="C:/Users/averi/.ssh/id_rsa.pub",
                               local_bind_address=('127.0.0.1', 8888)
                               ) as tunnel:
        with psycopg2.connect(dbname='admingf', user='postgres', password='12345', host='127.0.0.1',
                              port=8888) as connection:
            with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor_admin:
                callback(cursor_admin, response, *args)


def db_connect(sql_req):
    conn = psycopg2.connect(dbname='gf_production', user='developer', password='Pfbnk8YyU6yzUUxy',
                            host='192.168.0.22', port='5432')
    cursor = conn.cursor()
    cursor.execute(sql_req)
    records = cursor.fetchall()
    cursor.close()
    return records