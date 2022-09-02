from graph.query_graph import run_query


def get_mints(address):
    query = """
    
    {
      mints(where: {origin:\"""" + address + """\"}) {
        timestamp
        transaction {
          id
        }
        pool {
          id
        }
        token0 {
          symbol
          decimals
        }
        token1 {
          symbol
          decimals
        }
        amount,
        amount0,
        amount1,
        amountUSD,
        tickLower,
        tickUpper
      }
    }"""
    result = run_query(query)
    return result['mints']
