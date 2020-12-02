#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Piolink Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: pask_ntp
short_description: Configuring NTP client setting
description:
    - You can configure NTP client setting of the PAS-K.
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
    status:
        description:
            - Enter whether to use the NTP client service.
            - The value should be 'disable' or 'enable'.
        type: str
    primary_server:
        description:
            - Enter the NTP primary-server IP address.
        type: str
    secondary_server:
        description:
            - Enter the NTP secondary-servery IP address.
        type: str
    minpoll:
        description:
            - Enter the minimum value for the NTP synchronization period.
            - The value should be entered as an exponent of 2.
        type: str
    maxpoll:
        description:
            - Enter the maximum value for the NTP synchronization period.
            - The value should be entered as an exponent of 2.
        type: str

requirements:
    - requests
'''

EXAMPLES = r'''
---
- name: Ntp Test
  hosts: all
  connection: local
  collections:
  - piolink_yhoh.pask_test

  tasks:
  - name: ntp
    pask_ntp:
      prest_ip: "{{ansible_host}}"
      prest_port: "{{ansible_port}}"
      user_id: "{{user_id}}"
      user_pw: "{{user_pw}}"
      primary_server: "192.168.0.10"
      secondary_server: "192.168.0.20"
      minpoll: "4"
      maxpoll: "8"
      status: "disable"
'''

RETURN = r'''
#
'''

from ansible_collections.piolink_yhoh.pask_test.plugins.module_utils.pask_module import PaskModule,\
    make_module_args, try_except


mostouter_params = [
    'status', 'primary_server', 'secondary_server', 'minpoll',
    'maxpoll'
]

module_args = make_module_args(mostouter_params)

name = 'ntp'


class PaskNtp(PaskModule):
    def __init__(self, name, module_args):
        super(PaskNtp, self).__init__(name, module_args)

    @try_except
    def run(self):
        data = self.make_data(self.module.params)
        self.resp = self.put(self.url, data)


def main():

    ntp = PaskNtp(name, module_args)
    ntp.set_param()
    ntp.run()
    ntp.set_result()


if __name__ == '__main__':
    main()
