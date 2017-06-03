#!/usr/bin/python
from wakeonlan import wol
import time, argparse, paramiko


parser = argparse.ArgumentParser()
parser.add_argument('-w', action='store_true', dest='wakeup')
parser.add_argument('-s', action='store_true', dest='shutdown')
args = parser.parse_args()


if args.wakeup:
    print 'Waking up ESXI Server'
    wol.send_magic_packet('f0.4d.a2.3c.f1.eb')

if args.shutdown:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.178.5', username='root', password='Mike8ang!')
    stdin, stdout, stderr = ssh.exec_command('powerOffVms && halt')
    print 'Shutting down ESXi Server'
    ssh.close()
