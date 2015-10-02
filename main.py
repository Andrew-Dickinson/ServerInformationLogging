__author__ = 'Andrew'

import ping
import math
import socket
import datetime
import time
import psutil
import tsquery
from utility_functions import csv_store, log


def run():
    while True:
        timestamp = str(datetime.datetime.now().replace(microsecond=0))
        try:
            google_delay = ping.ping('www.google.com', timeout=2000)
            google_raw = 1000*google_delay
            google_processed = str(int(math.floor(google_raw)))
            router_delay = ping.ping('192.168.1.1', timeout=2000)
            router_raw = 1000*router_delay
            router_processed = str(int(math.floor(router_raw)))
            localhost_delay = ping.ping('www.andrewdickinson.us', timeout=2000)
            localhost_raw = localhost_delay*1000
            localhost_processed = str(int(math.floor(localhost_raw)))
            cpu_use = psutil.cpu_percent(interval=1)
            ram_use = psutil.virtual_memory().percent

            ts_data = tsquery.query()
            out = timestamp + " Google: " + google_processed + " Local Router: " + router_processed + " localhost: " + \
                              localhost_processed + " CPU: " + str(cpu_use) + "%" + " RAM: " + str(ram_use) + "%" \
                              " TS Users: " + ts_data['connected_users'] + " Avg TS ping: " + ts_data['avg_ping'] + \
                              " TS Bandwidth Out: " + ts_data['bandwidth_up'] + " TS Bandwidth In: " + \
                              ts_data['bandwidth_down'] + " </br>" + '\n '

            out = out.replace(' 0 ', ' <1 ')
            log(out)

            csv_store([timestamp, google_raw, router_raw, localhost_raw, cpu_use, ram_use,
                       ts_data['avg_ping'], ts_data['bandwidth_down'],
                       ts_data['bandwidth_up'], ts_data['connected_users']])

        # except TypeError:
        #     print "Error"
        #     log(str(datetime.datetime.now().replace(microsecond=0)) + " Error2</br>" + "\n")
        #     csv_store([timestamp, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        except socket.error, e:
            print "Ping Error:" + str(e)
            log(str(datetime.datetime.now().replace(microsecond=0)) + " Error" + "</br>" + '\n')
            csv_store([timestamp, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        except EOFError:
            print "TS Connection Issue"
            log(str(datetime.datetime.now().replace(microsecond=0)) + " Error3" + "</br>" + '\n')
            csv_store([timestamp, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        time.sleep(10)

run()