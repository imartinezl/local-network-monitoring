import os
import json
from datetime import datetime

source = '/home/pi/Desktop/local-network-monitoring/'
current_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S') #.%f

# Wifi network analysis
print("######### Wifi network analysis ##########")
import iwlist

content = iwlist.scan(interface='wlan0')
cells = iwlist.parse(content)
essid_list = ['MOVISTAR_67E6','MOVISTAR_67E6b']
with open(source + 'wifi.csv', 'a+') as outfile:
    for essid in essid_list:
        signal_level_dBm, signal_total, signal_quality = '', '', ''
        for cell in cells:
            if cell['essid'] == essid:
                signal_level_dBm = cell['signal_level_dBm']
                signal_total = cell['signal_total']
                signal_quality = cell['signal_quality']
        #to_save = {'time': current_time, 'essid': essid, 'signal_total': signal_total, 'signal_level_dBm': signal_level_dBm, 'signal_quality': signal_quality}
        #json.dump(to_save, outfile)
        outfile.write(current_time + ',' + essid + ',' + signal_total + ',' + signal_level_dBm + ',' + signal_quality + '\n')