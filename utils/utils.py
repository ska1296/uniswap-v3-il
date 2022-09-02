from numpy import divide


def get_eth_per_token(amount0, amount1, token1):
    return divide(amount0, amount1) if token1 == 'WETH' else divide(amount1, amount0)
