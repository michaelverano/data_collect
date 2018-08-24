#!/usr/bin/python
#coin_market_cap.py - collects data for btc, eth, ltc, and xrp from coin market cap.

def get_market_caps(requests):
    crypto = ['bitcoin', 'litecoin', 'ethereum', 'ripple']
    link = 'https://api.coinmarketcap.com/v1/ticker/'

    data = {}
    for coins in crypto:
        r = requests.get(link + coins)

        data[coins] = r.json()[0]

    return data
