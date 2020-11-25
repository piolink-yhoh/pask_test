#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Piolink.Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: pask_real
short_description: Configuring real server setting
description:
    - You can configure real server setting of the PAS-K.
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
            - Enter the real server id.
        required: true
        type: str
    rip:
        description:
            - Enter the real server ip address.
        required: true
        type: str
    name:
        description:
            - Enter the real server name.
        type: str
    rport:
        description:
            - Enter the real server port number.
        type: str
    mac:
        description:
            - Enter the real server mac address.
        type: str
    interface:
        description:
            - Enter the vlan interface connected to the real server.
        type: str
    priority:
        description:
            - Enter the priority of the real server.
        type: str
    weight:
        description:
            - Enter the weight of ther real server.
            - The value is used when the lb-method is 'wlc' or 'wrr'.
        type: str
    graceful_shutdown:
        description:
            - Enter whether to use the graceful-shudwon function.
            - The value should be 'enable' or 'disable'.
        type: str
    max_connection:
        description:
            - Enter the maximum number of sessions of the real server.
        type: str
    upload_bandwidth:
        description:
            - Enter the maximum upload-bandwidth of the real server.
        type: str
    download_bandwidth:
        description:
            - Enter the maximum download-bandwidth of the real server.
        type: str
    domain_filter:
        description:
            - Enter the domain filter id.
        type: str
    pool_size:
        description:
            - Enter the maximum number of connections to allow on the real server.
        type: str
    pool_age:
        description:
            - Enter the keep-alive time of connections.
        type: str
    pool_reuse:
        description:
            - Enter the number of times the connection is reused.
        type: str
    pool_srcmask:
        description:
            - Enter the source subnet mask of the connection.
        type: str
    src_natip:
        description:
            - Enter the source NAT ip of the real server.
        type: str
    backup:
        description:
            - Enter the id of the backup real server.
        type: str
    status:
        description:
            - Enter whether to use real server option.
            - The value should be 'enable' or 'disable'.
        type: str
    health_check:
        description:
            - Enther the health-check information.
        type: list
        elements: dict

        suboptions:
            id:
                description:
                    - Enter the health-check id.
                required: true
                type: str
    nat:
        description:
            - Enter the nat information of the real server.
            - The nat rule is applied only when the real server is used in gwlb.
        type: list
        elements: dict

        suboptions:
            id:
                description:
                    - Enter the id of the nat rule.
                type: str
            type:
                description:
                    - Enter the type of the nat rule.
                    - The value should be 'one-to-one-nat' or 'source-nat'.
                type: str
            priority:
                description:
                    - Enter the priority of the nat rule.
                type: str
            sip:
                description:
                    - Enter the source ip address and the number of the netmask bits.
                    - If you enter 'source-nat' as a type, you can set this value.
                type: str
            dip:
                description:
                    - Enter the destination ip address and the number of the netmask bits.
                    - If you enter 'source-nat' as a type, you can set this value.
                type: str
            protocol:
                description:
                    - Enter the protocol type of the packet to which the nat rule applies.
                    - If you enter 'source-nat' as a type, you can set this value.
                    - The value should be 'icmp', 'tcp', 'udp' or 'all'.
                type: str
            natip:
                description:
                    - Enter the source nat ip address.
                    - If you enter 'source-nat' as a type, you can set this value.
                type: str
            status:
                description:
                    - Enter whether to use the nat rule.
                    - The value should be 'enable' or 'disable'.
                type: str
            external_ip:
                description:
                    - Enter the external ip address.
                    - If you enter 'one-to-one-nat' as a type, you can set this value.
                type: str
            internal_ip:
                description:
                    - Enter the Inernal ip address.
                    - If you enter 'one-to-one-nat' as a type, you can set this value.
                type: str

    state:
        description:
            - Enter the status of this configuration.
            - If you want to delete this PAS-K configuration, enter 'absent',
            - otherwise, you can enter 'present' or you don't have to do enter anything.
        type: str

requirements:
    - requests
'''

EXAMPLES = r'''
---
- name: create real
  connection: local
  hosts: targets
  collections:
  - piolink_yhoh.pask_test

  tasks:
  - name: Create real
    pask_real:
      prest_ip: "{{ansible_host}}"
      prest_port: "{{ansible_port}}"
      user_id: "{{user_id}}"
      user_pw: "{{user_pw}}"
      id: "101"
      rip: "172.16.123.24"
      rport: "5544"
      priority: "30"
      weight: "50"
      graceful_shutdown: "enable"
      max_connection: "12"
      upload_bandwidth: "100000"
      download_bandwidth: "200000"
      domain_filter: "1, 2"
      pool_size: "100"
      pool_age: "200"
      pool_reuse: "300"
      pool_srcmask: "14"
      src_natip: "5.4.3.2"
      status: "disable"
      state: "present"

  - name: Delete real
    pask_real:
      prest_ip: "{{ansible_host}}"
      prest_port: "{{ansible_port}}"
      user_id: "{{user_id}}"
      user_pw: "{{user_pw}}"
      id: "101"
      rip: "172.16.123.24"
      state: "absent"
'''

RETURN = r'''
#
'''

from ansible_collections.piolink_yhoh.pask_test.plugins.module_utils.pask_module import PaskModule,\
    try_except, make_module_args
import os


inner_nat_param = [
    'id', 'type', 'priority', 'sip', 'dip', 'protocol', 'natip', 'status',
    'external_ip', 'internal_ip'
]
inner_nat_args = make_module_args(inner_nat_param)

inner_hc_args = dict(
    id=dict(type='str', required=True),
)

module_args = dict()
module_args = dict(
    id=dict(type='str', required=True),
    rip=dict(type='str', required=True),
    nat=dict(type='list', elements='dict', options=inner_nat_args),
    health_check=dict(type='list', elements='dict', options=inner_hc_args)
)

param_list = [
    'name', 'rport', 'mac', 'interface', 'priority', 'weight',
    'graceful_shutdown', 'max_connection', 'upload_bandwidth',
    'download_bandwidth', 'domain_filter', 'pool_size',
    'pool_age', 'pool_reuse', 'pool_srcmask', 'src_natip', 'backup',
    'state', 'status'
]
module_args.update(make_module_args(param_list))


name = 'real'


class PaskReal(PaskModule):
    def __init__(self, name, module_args):
        super(PaskReal, self).__init__(name, module_args)

    @try_except
    def run(self):
        url = os.path.join(self.url, self.module.params['id'])
        if self.module.params['state'] == "absent":
            self.ok_error_msg['delete'] = ['EntryDoesNotExist']
            resp = self.delete(url)
        else:
            data = dict()
            data = self.make_data(self.module.params, include_inner=True)
            resp = self.put(url, data)
        self.resp = resp


def main():
    real = PaskReal(name, module_args)
    real.set_param()
    real.run()
    real.set_result()


if __name__ == '__main__':
    main()
