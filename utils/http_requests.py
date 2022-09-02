from decimal import Decimal

import requests


def get_current_eth_price():
    url = "https://api.coinbase.com/v2/prices/ETH-USD/buy"

    payload = {}
    headers = {
        'Authorization': 'Bearer abd90df5f27a7b170cd775abf89d632b350b7c1c9d53e08b340cd9832ce52c2c'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return Decimal(response.json()['data']['amount'])
