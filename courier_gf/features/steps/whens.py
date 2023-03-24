import requests, json
from features.common import checks
from features.routes import api_routes_courier, headers
from behave import when


@when('Запрос "Доставлено"')
def step(context):
    response = requests.request(
        "POST",
        api_routes_courier.set_delivered + f'/{context.delivery_id}/deliver',
        headers=headers.generation_header(context))
    json_data = response.json()
    checks.check_status_code(response)
    #print(f'Запрос доставлено {json_data}')


@when('Запрос "запрос на отмену"')
def step(context):
    pass



@when('Запрос "перенос на завтра"')
def step(context):
    pass


@when('Запрос "Возрат на склад"')
def step(context):
    data = {"comment": "123"}
    response = requests.request(
        "POST",
        api_routes_courier.set_returned.format(context.delivery_id),
        headers=headers.generation_header(context), json=data)
    json_data = response.json()
    checks.check_status_code(response)
    print(json_data)