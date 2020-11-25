#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Piolink Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: pask_dns
short_description: Configuring DNS setting
description:
    - You can configure DNS setting of the PAS-K.
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
    retry:
        description:
            - Enter the number of retry attempts of the DNS query.
        type: str
    timeout:
        description:
            - Enter timeout of the DNS query in seconds.
        type: str
    id:
        description:
            - Enter the information of the DNS server.
        elements: dict
        type: list

        suboptions:
            id:
                description:
                    - Enter the DNS server id.
                required: true
                type: str
            ip:
                description:
                    - Enter the DNS server IP.
                required: true
                type: str

requirements:
    - requests
'''

EXAMPLES = r'''
---
- name: Dns Test
  hosts: all
  connection: local
  collections:
  - piolink_yhoh.pask_test

  tasks:
  - name: create dns ip
    pask_dns:
      prest_ip: "{{ansible_host}}"
      prest_port: "{{ansible_port}}"
      user_id: "{{user_id}}"
      user_pw: "{{user_pw}}"
      retry: "5"
      timeout: "10"
      id:
        - { id: "1", ip: "192.168.203.100" }
        - { id: "2", ip: "8.8.8.8" }
'''

RETURN = r'''
#
'''

from ansible_collections.piolink_yhoh.pask_test.plugins.module_utils.pask_module import PaskModule,\
    make_module_args, try_except

id_inner_args = dict(
    id=dict(type='str', required=True),
    ip=dict(type='str', required=True),
)

outermost_param_str = [
    'retry', 'timeout'
]
module_args = dict(
    id=dict(type='list', elements='dict', options=id_inner_args)
)
module_args.update(make_module_args(outermost_param_str))

name = 'dns'


class PaskDns(PaskModule):
    def __init__(self, name, module_args):
        super(PaskDns, self).__init__(name, module_args)

    @try_except
    def run(self):
        data = self.make_data(self.module.params, include_inner=True)
        self.resp = self.put(self.url, data)


def main():
    dns = PaskDns(name, module_args)
    dns.set_param()
    dns.run()
    dns.set_result()


if __name__ == '__main__':
    main()
