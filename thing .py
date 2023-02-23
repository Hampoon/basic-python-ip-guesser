#import pyping
import os
from faker import Faker #Module to generate IPv4 and IPv6 addresses 
import time
invalid = 0
valid = 0
ex = Faker()
while True:
    ip = ex.ipv4()
    ip2 = ex.ipv6()
#print('ipv4 address:- ',ip)
#print('ipv6 address:- ',ip2)

#This part pings the IP
    ip_to_check = (ip)

    testping = os.system(f'ping -c 1 -t 1 {ip_to_check}')
    # print(testping) #for testing
    if testping == 0:
        print('Good IP found, ipv4 is ' + ip + ' and ipv6 is ' + ip2)
        print(testping)
        valid = valid+1
        print(valid)
    else:
        print('Bad IP found, ipv4 is ' + ip + ' and ipv6 is ' + ip2)
        invalid = invalid+1
        print(invalid)
    print(f"good ips: {valid}, bad ips: {invalid}")
    time.sleep(0.1)