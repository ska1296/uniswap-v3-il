import requests


# function to use requests.post to make an API call to the subgraph url
def run_query(query):
    # endpoint where you are making the request
    request = requests.post('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'
                            '',
                            json={'query': query})
    if request.status_code == 200:
        return request.json()['data']
    else:
        raise Exception('Query failed. return code is {}.      {}'.format(request.status_code, query))
