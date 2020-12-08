#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Piolink Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: pask_health_check
short_description: Configuring health check setting
description:
    - You can configure health check setting of the PAS-K.
version_added: '2.10'
author:
    - Yohan Oh (@piolink-yhoh)

options:
    prest_ip:
        description:
            - Enter the PAS-K IP address.
        required: true
        type: str
    prest_port:
        description:
            - Enter the port number of PAS-K used for PREST-API.
        required: true
        type: str
    user_id:
        description:
            - Enter the PAS-K user id.
        required: true
        type: str
    user_pw:
        description:
            - Enter the PAS-K user password.
        required: true
        type: str
    id:
        description:
            - Enter the health-check ID.
        required: true
        type: str
    timeout:
        description:
            - Enter the health-check timeout.
        type: str
    interval:
        description:
            - Enter the health-check interval.
        type: str
    retry:
        description:
            - Enter the number of retransmissions packet to check health-check.
        type: str
    recover:
        description:
            - Enter the number of retransmissions packet to check recover fail.
            - If health-check is fail, recover check packet will be sent.
        type: str
    status:
        description:
            - Enter the status of the health-check.
            - The value should be 'enable' or 'disable'.
        type: str
    description:
        description:
            - Enter the description of the health-check.
        type: str
    sip:
        description:
            - Enter the source ip address of the health-check packet.
        type: str
    tip:
        description:
            - Enter the destination ip address of the health-check packet.
        type: str
    type:
        description:
            - Enter the type of the health-check.
            - The value should be act, arp, dhcp, dns, http, icmp, inact,
            - internal, link, ntp, radius-acct, radius-auth, snmp, ssl,
            - tcp, tftp or udp.
        type: str
    port:
        description:
            - Enter the destination port number of the health-check packet.
        type: str
    increase_icmp_id:
        description:
            - Enter whether to increase the icmp id
            - If you enter type as 'icmp', you can set this value.
        type: str
    mac:
        description:
            - Enter the source mac address between PAS-K and DHCP server.
            - If you enter type as 'dhcp', you can set this value.
        type: str
    half_open:
        description:
            - Enter whether to use TCP half-open option.
            - If you enter type as 'tcp', you can set this value.
        type: str
    send:
        description:
            - Enter the data to be sent to the real server.
            - The value are ASCII strings and can be assigned up to 128 characters.
            - If you enter type as 'tcp', 'ssl' or 'udp', you can set this value.
        type: str
    expect:
        description:
            - Enter the data you will receive from the real server.
            - The value are ASCII strings and can be assigned up to 128 characters.
            - If you enter type as 'tcp', 'udp', 'ssl', 'http' or 'tftp', you can set this value.
        type: str
    unexpect:
        description:
            - Enter the data you will receive from the real server to be considered fail.
            - The value are ASCII strings and can be assigned up to 128 characters.
            - If you enter type as 'tcp', 'udp', 'ssl', 'http' or 'tftp', you can set this value.
        type: str
    source_port_min:
        description:
            - Enter the minimum port number of tcp health-check packet.
            - If you enter type as 'tcp', you can set this value.
        type: str
    source_port_max:
        description:
            - Enter the maximum port number of tcp health-check packet.
            - If you enter type as 'tcp', you can set this value.
        type: str
    packets:
        description:
            - Enter the number of udp packet to check health-check.
            - If you enter type as 'udp', you can set this value.
        type: str
    uri:
        description:
            - Enter the uri of the real server to request data.
            - If you enter type as 'http' or 'https', you can set this value.
        type: str
    host:
        description:
            - Enter the host field in http request header section.
            - If you enter type as 'http' or 'https', you can set this value.
        type: str
    user_agent:
        description:
            - Enter the user-agent field in http request header section.
            - If you enter type as 'http' or 'https', you can set this value.
        type: str
    status_code:
        description:
            - Enter the http status code you will receive from the real server.
            - If you enter type as 'http' or 'https', you can set this value.
        type: str
    content_length:
        description:
            - Enter the http content-length field in http header.
            - If you enter type as 'http', you can set this value.
        type: str
    filename:
        description:
            - Enter the name of the file to download by connecting to the TFTP server.
            - If you enter type as 'tftp', you can set this value.
        type: str
    tolerance:
        description:
            - Enter the time difference between the real server and the PAS-K in seconds.
            - If you enter type as 'ntp', you can set this value.
        type: str
    update_delay:
        description:
            - Enter the frequency in seconds at which the real server updates time information.
            - If you enter type as 'ntp', you can set this value.
        type: str
    radius_auth_name:
        description:
            - Enter the user ID to be used when connecting to the RADIUS server for authentication.
            - If you enter type as 'radius', you can set this value.
        type: str
    radius_auth_passwd:
        description:
            - Enter the user password to be used when connecting to the RADIUS server for authentication.
            - If you enter type as 'radius', you can set this value.
        type: str
    radius_auth_secret:
        description:
            - Enter the secret password to be used when connecting to the RADIUS server for authentication.
            - If you enter type as 'radius', you can set this value.
        type: str
    radius_acct_secret:
        description:
            - Enter the secret password to be used
            - when connecting to the RADIUS server for accounting.
            - If you enter type as 'radius', you can set this value.
        type: str
    oid:
        description:
            - Enter the oid of the real server to check health-check.
            - If you enter type as 'snmp', you can set this value.
        type: str
    community:
        description:
            - Enter the snmp community to check health-check.
            - If you enter type as 'snmp', you can set this value.
        type: str
    record_type:
        description:
            - Enter the dns record-type to check health-check.
            - If you enter type as 'dns', you can set this value.
        type: str
    query:
        description:
            - Enter the dns query to check health-check.
            - If you enter type as 'dns', you can set this value.
        type: str
    version:
        description:
            - Enter the SSL version for SSL handshaking between client and real server.
            - The value must be 'ssl23', 'tls1', 'tls1.1' or 'tls1.2'.
            - If you enter type as 'ssl' or 'https', you can set this value.
        type: str
    validate:
        description:
            - Enter whether to perform certificate validation.
            - The value must be 'enable' or 'disable'.
            - If you enter typ as 'ssl', you can set this value.
        type: str
    common_name:
        description:
            - Enter the string to check the string is in the name of the certificate.
            - If you enter type as 'ssl' and enter validate as 'enable', you can set this value.
        type: str
    state:
        description:
            - Enter the status of this configuration.
            - If you want to delete this PAS-K configuration, enter absent,
            - otherwise, you can enter present or you don't have to do enter anything.
        type: str

requirements:
    - requests
'''

EXAMPLES = r'''
---
- name: Health-check Test
  hosts: all
  connection: local
  vars:
      - target_ip : "{{ansible_host}}"
      - port : "{{ansible_port}}"
  collections:
  - piolink_yhoh.pask_test

  tasks:
  - name: Create health-check
    pask_health_check:
      prest_ip: "{{ansible_host}}"
      prest_port: "{{ansible_port}}"
      user_id: "{{user_id}}"
      user_pw: "{{user_pw}}"
      id: "500"
      type: "tcp"
      half-open: "enable"
      increase_icmp_id: "enable"
      interval: "53"
      mac: "00:06:c4:94:02:27"
      port: "5004"
      retry: "2"
      timeout: "4"

  - name: Delete health-check
    pask_health_check:
      prest_ip: "{{ansible_host}}"
      prest_port: "{{ansible_port}}"
      user_id: "{{user_id}}"
      user_pw: "{{user_pw}}"
      id: "500"
      state: "absent"
'''

RETURN = r'''
#
'''

import os
from ansible_collections.piolink_yhoh.pask_test.plugins.module_utils.pask_module import PaskModule,\
    make_module_args, try_except

str_param_list = [
    'type', 'recover', 'timeout', 'interval', 'status', 'state', 'retry',
    'sip', 'tip', 'uri', 'host', 'user_agent', 'status_code', 'expect',
    'unexpect', 'content_length', 'increase_icmp_id', 'tolerance',
    'update_delay', 'oid', 'half_open', 'send', 'filename', 'packets',
    'radius_auth_name', 'port', 'radius_auth_passwd', 'radius_auth_secret',
    'radius_acct_secret', 'version', 'validate', 'common_name', 'description',
    'source_port_min', 'source_port_max', 'mac', 'community', 'record_type',
    'query'
]

module_args = dict(
    id=dict(type='str', required=True),
)

module_args.update(make_module_args(str_param_list))

name = 'health-check'


class PaskHealthcheck(PaskModule):
    def __init__(self, name, module_args):
        super(PaskHealthcheck, self).__init__(name, module_args)

    @try_except
    def run(self):
        if self.module.params['state'] == "absent":
            data = dict()
            url = os.path.join(self.url, self.module.params['id'])
            self.ok_error_msg['delete'] = ['EntryDoesNotExist']
            self.resp = self.prest.delete(url, data)
        else:
            data = self.make_data(self.module.params)
            url = os.path.join(self.url, self.module.params['id'])
            self.resp = self.prest.put(url, data)


def main():
    hc = PaskHealthcheck(name, module_args)
    hc.set_param()
    hc.run()
    hc.set_result()


if __name__ == '__main__':
    main()
