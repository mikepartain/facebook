#!/home/mikepartain/GIT/python/bin/python
import os, sys
from ciscoconfparse import *

# change the path to your configs below including the / at the end.
config_dir = '/home/mikepartain/configs/'

# Below we list all of the files in the config_dir defined above.  As
# we list each file, we parse it with CiscoConfParse to get the hostname
# interfaces with IP addresses configured, and then the actually IP 
# address that is configured for that interface.

for host in os.listdir(config_dir):
    # Here we join the directory with the filename.  CiscoConfParse expects to have the
    # absolute path to the file for parsing.
    filename = config_dir+host

    # parse will open each files and store the config in memory, so each time you parse
    # a file, the previous config in memory is dumped for the new one.
    parse = CiscoConfParse(filename)

    # Since we listed all of the files in the config directory, we can now parse them one
    # at a time.
    hostname = parse.find_objects('^hostname')
    for host in hostname:
        print host.text.split(' ',-1)[1]

    # below will get all interfaces that have a ip address configured
    # and will print the interface names and the ip address below the interface
    c_interfaces = parse.find_objects_w_child('^interface', 'ip address ')
    for c_interface in c_interfaces:
        print ' '+c_interface.text
        c_ip_address = parse.find_children_w_parents(c_interface.text+'$', 'ip address')
        for c_ip in c_ip_address:
            print '  '+c_ip
        print '!'
    
