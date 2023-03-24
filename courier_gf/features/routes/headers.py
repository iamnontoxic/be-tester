import requests, json
from features.common import constants
from features.routes import api_routes_courier

def generation_header(context):
    body = dict(login=constants.courier['login'], password=constants.courier['password'])
    response = requests.request('POST', api_routes_courier.login, data=body, headers=header_wo_auth)
    json_data = response.json()
    context.token = response.json()['token']
    return {
        'Accept': 'application/json', 'text/plain'
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + context.token
    }


header_wo_auth = {
    'Accept': 'application/json', 'text/plain'
    'Content-Type': 'application/json'
}


def generation_header_for_admin():
    return {
        'Accept': 'application/json', 'text/plain'
        'Content-Type': 'application/json',
        'X-Auth': 'uyEOeURLM2eN08XO5UIe'
    }


def generation_put_header_for_admin():
    return {
        'Accept': 'application/json', 'text/plain'
        'Content-Type': 'application/json',
        'X-Auth': 'uyEOeURLM2eN08XO5UIe',
        'X-HTTP-Method-Override': 'PUT'
    }