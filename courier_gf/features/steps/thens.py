import json
from behave import then
from features.common import constants, checks, connection_ssh_db
from features.steps import out_of_steps

@then('Получение токена')
def step(context):
    context.token = context.response.json()['token']



@then('Проверка получения токена')
def check(context):
    if context.response.json()['token'] == "":
        raise Exception('Отсутствует токен в ответе')
    else:
        assert True



@then('Доставка в статусе "Доставлено"')
def check(context):
    table_name = 'deliveries'
    connection_ssh_db.connect_ssh_db_admin(checks.check_create, context.delivery_id, table_name)
    connection_ssh_db.connect_ssh_db_admin(checks.check_delivery_status, context.delivery_id, table_name)
    connection_ssh_db.connect_ssh_db_admin(checks.set_cancel_delivery, context.delivery_id, table_name)


@then('Доставка в статусе "Возврат на склад"')
def check(context):
    table_name = 'deliveries'
    connection_ssh_db.connect_ssh_db_admin(checks.check_create, context.delivery_id, table_name)