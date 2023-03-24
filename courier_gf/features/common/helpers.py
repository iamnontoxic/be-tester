import requests

from features.routes import api_routes_courier, headers


# Получение токена
def auth(context):
    body = {'login': 'test@test.ru',
            'password': 'testsAreVeryGood!!11'}
    context.response = requests.request('POST', api_routes_courier.url_auth_courier, data=body,
                                        headers=headers.header_wo_auth)
    context.token = context.response.json()['token']
    return context.token


#
