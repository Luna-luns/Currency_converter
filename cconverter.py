import json
import requests


my_currency = input().strip().lower()
cache = {}

while True:
    currency_code = input().strip().lower()
    if not currency_code:
        break

    money = float(input().strip())

    url = f'http://www.floatrates.com/daily/{my_currency}.json'
    response = requests.get(url).text
    response = json.loads(response)

    if 'usd' in response:
        cache['usd'] = response['usd']['rate']

    if 'eur' in response:
        cache['eur'] = response['eur']['rate']

    print('Checking the cache...')

    if currency_code in cache:
        exchanged_money = round(money * cache[currency_code], 2)
        print(f'Oh! It is in the cache!\nYou received {exchanged_money} {currency_code.upper()}.')
    else:
        cache[currency_code] = response[currency_code]['rate']
        exchanged_money = round(money * cache[currency_code], 2)
        print(f'Sorry, but it is not in the cache!\nYou received {exchanged_money} {currency_code.upper()}.')
