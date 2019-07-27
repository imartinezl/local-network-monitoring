import json
from datetime import datetime

source = '/home/pi/Desktop/local-network-monitoring/'
current_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S') #.%f

# Wifi network analysis
print("######### Wifi network analysis ##########")
import iwlist

content = iwlist.scan(interface='wlan0')
cells = iwlist.parse(content)
with open(source + 'data/wifi_' + current_time + '.json', 'w') as outfile:
    json.dump(cells, outfile)

# Connected devices
print("######### Connected devices ##########")
import nmap
nm = nmap.PortScanner()
nm.scan(hosts='192.168.1.0/24', arguments='-sn')
output = []
with open(source + 'data/devices_' + current_time + '.json', 'w') as outfile:
    for h in nm.all_hosts():
        print(h)
        if 'mac' in nm[h]['addresses']:
            item = nm[h]['addresses']
            if nm[h]['vendor'].values():
                item['vendor'] = list(nm[h]['vendor'].values())[0]
            output.append(item)
    json.dump(output, outfile)
