# Calculate impermanent loss

This goes on to calculate impermanent loss for an address (considering only one asset). To define impermanent loss, it's the difference in value of assets after staking in a liquidity pool and the value of assets if they were just held.

```(price_staked/price_held - 1) * 100```

The program does the following:
1. Get address's staked assets (in terms of the other token)
2. Gets swaps after the address has added liquidity to the pool
3. For each swap, it calculates ETH's worth in terms of the other token
4. Gets current price of ETH in USD
5. Finds the % change as per formula above

## Assumptions:
1. The other asset is always a stable ERC-20 coin
2. The first token is always WETH
3. The data returned for swaps (from the graph) in a pool is already in the range of ticks in which the address provided liquidity

## Drawbacks:
1. Does not consider ticks
2. It calculates a change in value of ETH in terms of USD
3. It does not consider the other token at all in the calculation

Address used for testing: `0xadc8aaddf5dcf81366fcc0212c154dfbfde1ed13`
Entry point: impermanent-loss/app/app.py