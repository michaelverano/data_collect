#!/usr/bin/python
#log.py - creates a log file for logging when program initiates.

import os
import datetime
import csv

def create_log():
    """
    
    ###
    ### CHANGE THIS DIRECTORY ####
    ### os.chdir('YOUR DIRECTORY')
    ###

    if 'logs' not in os.listdir():
        os.makedirs('logs')
    
    os.chdir('./logs')
    
    log_file = open('log.csv', 'a')
    log_writer = csv.writer(log_file)
    log_writer.writerow(['Program Initiated - {}'.format(str(datetime.datetime.now()))])
    log_file.close()
    """

    raise "look at the log.py and change the directory"
