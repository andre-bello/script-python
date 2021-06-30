#!/usr/bin/python3
from pyzabbix import ZabbixAPI
import urllib3
from datetime import datetime 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

zapi = ZabbixAPI("http://127.0.0.1/zabbix") 
zapi.session.verify=False
zapi.login("zabbix_api", "ZBXpassw0rdAPI")
print("Connected to Zabbix API Version %s" % zapi.api_version())

hosts = zapi.host.get(
            search={"name":"API Server"},
            output=["hostid","name"]
        )
print (hosts)
hostid = hosts[0]["hostid"]
print ('HostID: ' + str(hostid))

items = zapi.item.get (
    hostids=hostid,
    output=["itemid","name","key_","flags"]
     )
print (items)
