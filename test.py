# -*- coding: utf-8 -*-

import requests

API_KEY = 'dgS3hBL4R3wc2ff1Gg0X2GsIUH5Gtw3wN33PYSTz25WVvUsO7mnuplZ0BSYs6uAFx3nZtnVzLWy4JgzMIcntVX'
BASE_URL = "https://api.ataix.kz"


def get_request(endpoint):
    url = f"{BASE_URL}{endpoint}"
    headers = {
        "API-KEY": API_KEY,
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Ошибка: {response.status_code}, {response.text}"
    except requests.exceptions.Timeout:
        return "Ошибка: Превышено время ожидания ответа от сервера"
    except requests.exceptions.RequestException as e:
        return f"Ошибка запроса: {e}"


def get_currencies():
    data = get_request("/api/currencies")
    res = data['result']
    currencies_count = 0
    print('Все валюты: ')
    for i in res:
        print(i['symbol'])
        currencies_count += 1
    print(f'Количество валют: {currencies_count}')

def get_symbols():
    data = get_request("/api/symbols")
    res = data['result']
    symbols_count = 0
    print('Все пары валют: ')
    for i in res:
        print(i['symbol'])
        symbols_count += 1
    print(f'Количество пар валют: {symbols_count}')


def get_prices():
    data = get_request("/api/prices")
    res = data['result']
    print('Цены монет: ')

    for i in res:
        print(i['symbol'].split('/')[0], ': ', i['lastTrade'],' ' ,i['symbol'].split('/')[1])


get_currencies()
print('----------------------------------------------------------------------------')
get_symbols()
print('----------------------------------------------------------------------------')
get_prices()

