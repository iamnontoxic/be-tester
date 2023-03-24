import requests
import json
from features.routes import api_routes_courier, headers
from features.common import checks, constants
from datetime import datetime, timedelta



# Вычисляем завтрашнюю дату
tomorrow = datetime.now() + timedelta(days=1)
# Форматируем дату в виде строки "YYYY-MM-DD"
tomorrow_str = tomorrow.strftime("%Y-%m-%d")
# Вычисляем сегодняшнюю дату
today = datetime.now()
# Форматируем дату в виде строки "YYYY-MM-DD"
today_str = today.strftime("%Y-%m-%d")



def get_courier_token(context):
    body = dict(login=constants.courier['login'], password=constants.courier['password'])
    response = requests.request('POST', api_routes_courier.login, data=body, headers=headers.header_wo_auth)
    json_data = response.json()
    context.token = response.json()['token']


def get_delivery_info(context):
    response = requests.request(
        "GET",
        api_routes_courier.get_delivery_info + f'/{context.delivery_id}/info',
        headers=headers.generation_header_for_admin())
    json_data = response.json()
    context.session_value = json_data["delivery"]["session"]
    checks.check_status_code(response)
    #print(json_data)



def change_delivery_date(context):
    data = {
    "delivery_date": today_str,
    "ignore_production_order": 0,
    "magnet_move": 0}
    response = requests.request(
        "POST",
        api_routes_courier.change_delivery_date + f'/{context.delivery_id}/change-delivery-date',
        headers=headers.generation_header_for_admin(),
        json=data)
    json_data = response.json()
    checks.check_status_code(response)
    #print(today_str)
    #print(json_data)





