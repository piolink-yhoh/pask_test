#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Piolink Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: pask_vlan
short_description: Configuring vlan setting
description:
    - You can configure vlan setting of the PAS-K.
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
    vid:
        description:
            - Enter the vlan ID.
        required: true
        type: str
    name:
        description:
            - Enter the vlan name.
        required: true
        type: str
    port:
        description:
            - Enter the port info to be include in the vlan.
        type: list
        elements: dict

        suboptions:
            name:
                description:
                    - Enter the port name.
                required: true
                type: str
            type:
                description:
                    - Enter the port type.
                    - The value should be 'tagged' or 'untagged'.
                required: true
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
- name: Interface Test
  hosts: all
  connection: local
  collections:
  - piolink_yhoh.pask_test

  tasks:
  - name: create vlan
    pask_vlan:
      prest_ip: "{{ansible_host}}"
      prest_port: "{{ansible_port}}"
      user_id: "{{user_id}}"
      user_pw: "{{user_pw}}"
      name: "test_vlan"
      vid: "2917"
      port:
        - name: "ge7"
          type: "untagged"

  - name: delete vlan
    pask_vlan:
      prest_ip: "{{ansible_host}}"
      prest_port: "{{ansible_port}}"
      user_id: "{{user_id}}"
      user_pw: "{{user_pw}}"
      name: "test_vlan"
      vid: "2917"
      state: "absent"
'''

RETURN = r'''
#
'''

import os
from ansible_collections.piolink_yhoh.pask_test.plugins.module_utils.pask_module import PaskModule,\
    try_except


inner_port_args = dict(
    name=dict(type='str', required=True),
    type=dict(type='str', required=True),
)

module_args = dict(
    vid=dict(type='str', required=True),
    name=dict(type='str', required=True),
    port=dict(type='list', elements='dict', options=inner_port_args),
    state=dict(type='str'),
)

name = 'vlan'


class PaskVlan(PaskModule):
    def __init__(self, name, module_args):
        super(PaskVlan, self).__init__(name, module_args)

    @try_except
    def run(self):
        url = os.path.join(self.url, self.module.params['name'])
        if self.module.params['state'] == "absent":
            self.ok_error_msg['delete'] = ['There is no vlan']
            self.resp = self.prest.delete(url)
        else:
            data = self.make_data(self.module.params)
            self.resp = self.prest.put(url, data)


def main():
    vlan = PaskVlan(name, module_args)
    vlan.set_param()
    vlan.run()
    vlan.set_result()


if __name__ == '__main__':
    main()
