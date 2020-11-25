#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Piolink.Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: pask_hostname
short_description: Configuring hostname setting
description:
    - You can configure hostname setting of the PAS-K.
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
    hostname:
        description:
            - Enter the hostname of the PAS-K.
        required: true
        type: str

requirements:
    - requests
'''

EXAMPLES = r'''
---
- name: Hostname Test
  hosts: all
  connection: local
  collections:
  - piolink_yhoh.pask_test

  tasks:
  - name: create hostname
    pask_hostname:
      prest_ip: "{{ansible_host}}"
      prest_port: "{{ansible_port}}"
      user_id: "{{user_id}}"
      user_pw: "{{user_pw}}"
      hostname: "switch_ansible"

  - name: rename hostname
    pask_hostname:
      prest_ip: "{{ansible_host}}"
      prest_port: "{{ansible_port}}"
      user_id: "{{user_id}}"
      user_pw: "{{user_pw}}"
      hostname: "switch"
'''

RETURN = r'''
#
'''

from ansible_collections.piolink_yhoh.pask_test.plugins.module_utils.pask_module import PaskModule,\
    try_except


module_args = dict(
    hostname=dict(type="str", required=True)
)

name = 'hostname'


class PaskHostname(PaskModule):
    def __init__(self, name, module_args):
        super(PaskHostname, self).__init__(name, module_args)

    @try_except
    def run(self):
        resp = None

        data = self.make_data(self.module.params)
        resp = self.put(self.url, data)
        self.resp = resp


def main():
    hostname = PaskHostname(name, module_args)
    hostname.set_param()
    hostname.run()
    hostname.set_result()


if __name__ == '__main__':
    main()
