import requests
import json
from datetime import datetime, timedelta
from features.common import checks, constants
from features.routes import api_routes_courier, headers
from features.steps import out_of_steps
from behave import given



# Вычисляем завтрашнюю дату
tomorrow = datetime.now() + timedelta(days=1)
# Форматируем дату в виде строки "YYYY-MM-DD"
tomorrow_str = tomorrow.strftime("%Y-%m-%d")
# Вычисляем сегодняшнюю дату
today = datetime.now()
# Форматируем дату в виде строки "YYYY-MM-DD"
today_str = today.strftime("%Y-%m-%d")



@given('Запрос на авторизацию')
def step(context):
    body = dict(login=constants.courier['login'], password=constants.courier['password'])
    context.response = requests.request('POST', api_routes_courier.login, data=body, headers=headers.header_wo_auth)
    checks.check_status_code(context.response)
    json_data = context.response.json()
    context.token = context.response.json()['token']
    print(context.token)



@given('Создание заказа, планирование, назначение курьера и выдача коробки')
def step(context):
    out_of_steps.create_task(context)
    out_of_steps.create_order(context)
    out_of_steps.delivery_set_planned(context)
    out_of_steps.close_task(context)
    out_of_steps.assign_courier(context)
    out_of_steps.give_box_to_courier(context)



@given('Создание обращения в КЦ')
def create_task(context):
    response = requests.request('GET', api_routes_courier.create_task, headers = headers.generation_header_for_admin())
    context.task_id = response.json()['taskId']
    checks.check_status_code(response)
    #print(f'task_id = {context.task_id}')

@given('Создание заказа')
def create_order(context):
    data = {
        "daysAmount": 2,
        "pricePlanId": constants.msk_plan_id["basic"],
        "deliveriesStartDate": tomorrow_str,
        "deliveriesStartDateType": "evening",
        "taskId": context.task_id}
    response = requests.request(
        "POST",
        api_routes_courier.create_order + f"/{context.task_id}/related-orders/create",
        headers=headers.generation_header_for_admin(),
        json=data)
    json_data = response.json()
    context.order_id = json_data["order"]["deliveries"][0]["order_id"]
    context.delivery_id = json_data["order"]["deliveries"][0]["id"]
    checks.check_status_code(response)
    print(f'order_id = {context.order_id}')
    print(f'delivery_id = {context.delivery_id}')


@given('Запланировать доставку')
def delivery_set_planned(context):
    data = {"disableCheckLimits":False}
    response = requests.request(
        "POST",
        api_routes_courier.set_planned + f'/{context.delivery_id}/set-planned',
        headers=headers.generation_put_header_for_admin(),
        json=data)
    json_data = response.json()
    checks.check_status_code(response)
    #print(json_data)

@given('Закрыть обращение')
def close_task(context):
    data = {"feedback_reasons":[],"comment":""}
    response = requests.request(
        "POST",
        api_routes_courier.close_task + f'/{context.task_id}/close',
        headers=headers.generation_header_for_admin(),
        json=data)
    json_data = response.json()
    checks.check_status_code(response)
    out_of_steps.change_delivery_date(context)
    out_of_steps.get_delivery_info(context)



@given('Назначить курьера на доставку')
def assign_courier(context):
    data = {"driver_id":constants.courier['id'],"ids":[context.delivery_id],"force":True,
            "original_dates_with_session_hash":{context.delivery_id:{"delivery_date":today_str,"session":context.session_value}}}
    response = requests.request(
        "POST",
        api_routes_courier.assign_courier,
        headers=headers.generation_header_for_admin(),
        json=data)
    json_data = response.json()
    #print(json_data)
    checks.check_status_code(response)
    #if json_data["success"] is True:
    #    print(f'Доставка {context.delivery_id} назначена на курьера {constants.courier["id"]}')


@given('Выдать коробку курьеру')
def give_box_to_courier(context):
    response = requests.request(
        "POST",
        api_routes_courier.give_box_to_courier + f'/{context.delivery_id}/force-ship-own-items',
        headers=headers.generation_header_for_admin())
    json_data = response.json()
    checks.check_status_code(response)
    #print(json_data)



