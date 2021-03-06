#!//home/mikepartain/GIT/python/bin/python

#!/Users/mikepartain/git/python/bin/python
from scapy.all import *
from netaddr import *
import sys
from datetime import datetime

def main():
    try:
        network = raw_input('What network would you like to scan? (ie 192.168.1.0/24): ')
        if IPNetwork(network):
            print 'Valid network entered.'
            scan(network)
        else:
            print 'Invalid network, please try again'
            main()

    except KeyboardInterrupt:
        print '\nExiting due to user break.'

    except AddrFormatError:
        print 'Invalid network, please try again'
        main()


def scan(network):
    starttime = datetime.now()
    print 'Starting scan at: ', starttime
    conf.verb = 0
    for ip in IPNetwork(network).iter_hosts():
        packet = IP(dst=ip, ttl=20) / ICMP()
        reply = sr1(packet)
        if ip in reply.src:
            print reply.src +' is online.'
    #     print '%s' % ip


    # from scapy.all import *
    # conf.verb = 0
    # for ip in range(0, 256):
    #     packet = IP(dst="192.168.0." + str(ip), ttl=20) / ICMP()
    #     reply = sr1(packet)
    #     if "192.168." in reply.src:
    #         print reply.src, "is online"

main()
