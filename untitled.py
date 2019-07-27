import nmap
import json

nm = nmap.PortScanner()
nm.scan(hosts='192.168.1.0/24', arguments='-sn -r')
output = []
with open('output.txt', 'a') as outfile:
    for h in nm.all_hosts():
        print(h)
        if 'mac' in nm[h]['addresses']:
            item = nm[h]['addresses']
            if nm[h]['vendor'].values():
                item['vendor'] = list(nm[h]['vendor'].values())[0]
            output.append(item)
    json.dump(output, outfile)
