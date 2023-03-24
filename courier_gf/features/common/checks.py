import datetime
import time
from datetime import timedelta, datetime
from requests.exceptions import HTTPError
from features.common import helpers, connection_ssh_db


def check_status_code(response):
    try:
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        raise HTTPError
    except Exception as err:
        print(f'Other error occurred: {err}')
        raise Exception
    else:
        if response.status_code == 201 or 200:
            assert True
        else:
            raise Exception


def check_create(cursor, variable_id, table_name):
    resp = variable_id
    cursor.execute('SELECT * FROM ' + table_name + ' where id = %(id)s', {'id': resp})
    row = cursor.fetchone()
    if row['id']:
        print(f'В бд в таблице {table_name} есть запись с id {variable_id}')
    else:
        raise Exception('Database Test: Failed')



def check_delete(cursor, variable_id, table_name):
    resp = variable_id
    cursor.execute('SELECT EXISTS(SELECT * FROM ' + table_name + ' where id = %(id)s)', {'id': resp})
    row = cursor.fetchone()
    if row['exists'] == False:
        assert True
    else:
        cursor.execute('SELECT * FROM ' + table_name + ' where id = %(id)s', {'id': resp})
        row = cursor.fetchone()
        if row['deleted_at']:
            assert True
        else:
            raise Exception('Database Test: Failed')


def set_cancel_delivery(cursor, variable_id, table_name):
    resp = variable_id
    cursor.execute('UPDATE ' + table_name + ' SET status_id = 6 WHERE id = %(id)s', {'id': resp})
    row_count = cursor.rowcount
    if row_count > 0:
        print(f'Установили в таблице {table_name} у id {variable_id} status_id = 6 (canceled)')
    else:
        raise ValueError(f'Нет записи с id {variable_id} в таблице {table_name}')


def check_delivery_status(cursor, variable_id, table_name):
    cursor.execute('SELECT status_id FROM ' + table_name + ' WHERE id = %(id)s', {'id': variable_id})
    row = cursor.fetchone()
    if row['status_id'] == 4:
        print(f'В таблице {table_name} у id {variable_id} статус доставки = 4 (Доставлено)')
    else:
        raise ValueError(f'В таблице {table_name} у id {variable_id} статус доставки не равен 4')