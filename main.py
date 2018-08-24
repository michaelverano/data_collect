#!/home/mverano/data_collect/bin/python
# main.py - controller for data_collect.py

from modules import *
import requests


### COLLECT DATA FROM DIFFERENT EXCHANGES ###
bitstamp_data = bitstamp.main(requests)
binance_data = binance.main(requests)
market_cap = coin_market_cap.get_market_caps(requests)


write_data.navigate_to_data_folder()

### WRITE DATA TO CSV ###
write_data.bitstamp_to_csv(bitstamp_data, headers.bitstamp_headings)
write_data.binance_to_csv(binance_data, headers.binance_headings)
write_data.coin_market_cap(market_cap, headers.coin_market_cap_headings)

### TO DO ###
log.create_log()
