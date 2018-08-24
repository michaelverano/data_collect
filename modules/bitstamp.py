#!/usr/bin/python
# bitstamp.py - controller for using the bitstamp API.

# collects data only.

def main(requests):

    coins = ['btcusd', 'ethusd', 'ltcusd', 'xrpusd']

    json_data = {}
    for coin in coins:
        # json_data.append(coin) # test
        #print('getting requests')
        r = requests.get('https://www.bitstamp.net/api/v2/ticker/' + coin)

        #print('appending json_data')
        json_data[coin] = r.json()

        #print('appending complete')
        
        
    return json_data
