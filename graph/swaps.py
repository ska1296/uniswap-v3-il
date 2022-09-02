from graph.query_graph import run_query


def get_swaps(pool_id, timestamp):
    query = """
    
{
   swaps(where: {pool: \"""" + pool_id + """\", timestamp_gt: \"""" + timestamp + """\"}) {
    amount0
    amount1
    tick
    timestamp
    token0 {
      symbol
    }
    token1 {
      symbol
    }
   }
 } """
    result = run_query(query)
    return result['swaps']
