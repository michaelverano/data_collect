#!/usr/bin/python
# write_data.py - controller for writing data from collected data.

import csv
import os

def write_headers(file_name, headers):
    new_file = open(file_name, 'a')
    csv_writer = csv.writer(new_file)
    csv_writer.writerow(headers)
    new_file.close()

def navigate_to_data_folder():
    raise "change the directory on the write_data.navigate_to_data_folder"
    #os.chdir('<YOUR DIRECTORY HERE')
    

def bitstamp_to_csv(bitstamp_data, headers):
    for coin in bitstamp_data:
        file_name = coin+'.csv'
        if file_name not in os.listdir():
            write_headers(file_name, headers)
        
        coin_data = open(file_name, 'a')

        csv_writer = csv.writer(coin_data)

        headers = ['low', 'high', 'last', 'open', 'bid', 'ask', 'volume', 'vwap', 'timestamp']
        items = [bitstamp_data[coin][header] for header in headers]

        #csv_writer.writerow(order)
        csv_writer.writerow(items)
        
        coin_data.close()

def binance_to_csv(binance_data, headers):
    coin_of_interest = ['BTCUSDT', 'LTCUSDT', 'ETHUSDT', 'XRPUSDT']
    api_time = binance_data['time']
    
    for coin in coin_of_interest:
        file_name = coin+'.csv'
        if file_name not in os.listdir():
            write_headers(file_name, headers)

        coin_data = open(file_name, 'a')
        csv_writer = csv.writer(coin_data)

        ### HEADINGS ###
        # price, time
        items = [binance_data[coin], api_time]

        #csv_writer.writerow(['price', 'time'])
        csv_writer.writerow(items)

        coin_data.close()

def coin_market_cap(market_cap, headings):
    for coin in market_cap:

        file_name = coin+'_market_cap.csv'
        if file_name not in os.listdir():
            write_headers(file_name, headings)

        coin_data = open(file_name, 'a')

        csv_writer = csv.writer(coin_data)

        # HEADINGS
        # name, id, price_usd, marketcap_usd,
        # percent_change_1h, percent_change_7d, percent_change_24h,
        # total_supply, max_supply, available_supply
        # last updated, symbol, price_usd
        
        # headings = ['name', 'id', 'symbol', 'price_usd', 'market_cap_usd',
        #             'percent_change_1h', 'percent_change_7d', 'percent_change_24h',
        #             'total_supply', 'max_supply', 'available_supply', 'last_updated',]
        
        row = []
        for heading in headings:
            row.append(market_cap[coin][heading])

        csv_writer.writerow(row)
        coin_data.close()
