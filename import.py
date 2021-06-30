#!/usr/bin/python3
import urllib3
from pyzabbix import ZabbixAPI,ZabbixAPIException

 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
zapi = ZabbixAPI("http://127.0.0.1/zabbix")
zapi.session.verify=False
zapi.login("zabbix_api", "ZBXpassw0rdAPI")
print("Connected to Zabbix API Version %s" % zapi.api_version())
# Read file
file = open('/usr/lib/zabbix/apiscripts/hosts.txt').read().splitlines()
# Create a host group
host_group = zapi.hostgroup.create (name = "Imported hosts")
# Create hosts
for line in file:
        line_list = line.split()
        host_ip = line_list[0]
        host_dns = line_list[2]
        host_name = line_list[1]
        try:
                result = zapi.host.create (
                        host = host_name,
                        groups = [{"groupid": host_group['groupids'][0]}],
                        interfaces = [{"type":1,"main":1,"useip":1,"ip":host_ip,"dns":host_dns,"port":10050}]
                )
        except  ZabbixAPIException as e:
                print ('host ' + host_name + ' not created: ' + str(e))
        else:
                print ('host ' + host_name + ' created: ' + str(result))
