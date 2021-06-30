#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#author: Janssen dos Reis Lima
#modified André Bello

from pyzabbix import ZabbixAPI
import csv
from progressbar import ProgressBar, Percentage, ETA, ReverseBar, RotatingMarker, Timer
 
zapi = ZabbixAPI("http://127.0.0.1/zabbix")
zapi.login(user="Admin", password="zabbix")
arq = csv.reader(open('/usr/lib/zabbix/apiscripts/hosts.csv'))
linhas = sum(1 for linha in arq)
 
f = csv.reader(open('/usr/lib/zabbix/apiscripts/hosts.csv'), delimiter=',')
bar = ProgressBar(maxval=linhas,widgets=[Percentage(), ReverseBar(), ETA(), RotatingMarker(), Timer()]).start()
i = 0
 
for [hostname,tag] in f:
    if tag == 'Windows':
        hostcriado = zapi.host.create(
        host= hostname,
        status= 1,
        interfaces=[{"type": 1,"main": "1","useip": 1,"ip": "127.0.0.1","dns": "","port": 10050}],
        #groups=[{"groupid": 21}],
        tags = [{"tag":"SO","value":tag}],
        groups=[{ "groupid": 24}],
        templates=[{"templateid": 10081}],
        )
    else:
        hostcriado = zapi.host.create(
        host= hostname,
        status= 1,
        interfaces=[{"type": 1,"main": "1","useip": 1,"ip": "127.0.0.1","dns": "","port": 10050}],
        #groups=[{"groupid": 21}],
        tags = [{"tag":"SO","value":tag}],
        groups=[{"groupid": 2}],
        templates=[{"templateid": 10001}]
        )
        
    i += 1
    bar.update(i)
bar.finish
print (" ")
zapi.user.logout()
