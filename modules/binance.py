#!/usr/bin/python
#binance.py - collects data from binance API (i.e. just the link).

from datetime import datetime


def main(requests):
    binance_link = 'https://api.binance.com/api/v1/ticker/price?symbol='
    data = collect_data(requests, binance_link)
    data['time'] =  str(datetime.now())
    
    json_xrpbtc = collect_xrp(requests, binance_link)
    data['XRPUSDT'] = convert_xrpbtc(json_xrpbtc['XRPBTC'], data['BTCUSDT'])

    return data
    
def collect_data(requests, binance_link):
    listed_data = [
        requests.get(binance_link+'BTCUSDT'),
        requests.get(binance_link+'LTCUSDT'),
        requests.get(binance_link+'ETHUSDT'),]

    data = {}

    for items in listed_data:
        data[items.json()['symbol']] = float(items.json()['price'])
        
    return data

    
# Collect XRP/BTC data.
def collect_xrp(requests, binance_link):
   json_xrpbtc = requests.get(binance_link+'XRPBTC').json()
   return {json_xrpbtc['symbol'] : float(json_xrpbtc['price'])}
   
# convert XRP/BTC to XRP BTC.
def convert_xrpbtc(json_xrpbtc, btc_price):
    """Convert xrpbtc to xrpusdt"""
    return json_xrpbtc * btc_price 
