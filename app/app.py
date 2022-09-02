from decimal import Decimal

from numpy import divide, multiply, subtract

from graph.mints import get_mints
from graph.swaps import get_swaps
from utils.http_requests import get_current_eth_price
from utils.utils import get_eth_per_token


def get_swaps_for(pool_id, start_time):
    return get_swaps(pool_id, start_time)


def get_mint_details(address):
    mint_0 = get_mints(address)[0]
    return mint_0['pool']['id'], mint_0['timestamp']


def get_change_over_swaps(swaps):
    list_eth_per_token = []
    for element in swaps:
        eth_per_token = get_eth_per_token(Decimal(element['amount0']), Decimal(element['amount1']),
                                          element['token1']['symbol'])
        list_eth_per_token.append({'eth_per_token': eth_per_token * -1, 'timestamp': element['timestamp']})

    return list_eth_per_token


if __name__ == '__main__':
    pool_0, start_time = get_mint_details(input('user address\n'))
    swaps = get_swaps_for(pool_0, start_time)
    price_change_over_swaps = get_change_over_swaps(swaps) # plug historic price data here to calculate il over swaps
    current_eth_price = get_current_eth_price()
    print(multiply(100, subtract(divide(price_change_over_swaps[-1]['eth_per_token'], current_eth_price), 1)))

