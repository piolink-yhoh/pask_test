#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Piolink.Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: pask_reboot
short_description: Rebooting the PAS-K machine.
description:
    - You can reboot the PAS-K machine.
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
    verify:
        description:
            - If you want to reboot the PAS-K machine, enter 'yes'.
        required: true
        type: str

requirements:
    - requests
'''

EXAMPLES = r'''
---
- name: Reboot Test
  hosts: all
  connection: local
  collections:
  - piolink_yhoh.pask_test

  tasks:
  - name: Reboot PAS-K
    pask_reboot:
      prest_ip: "{{ansible_host}}"
      prest_port: "{{ansible_port}}"
      user_id: "{{user_id}}"
      user_pw: "{{user_pw}}"
      verify: "yes"
'''

RETURN = r'''
#
'''

from ansible_collections.piolink_yhoh.pask_test.plugins.module_utils.pask_module import PaskModule,\
    try_except


module_args = dict(
    verify=dict(type="str", required=True)
)

name = 'reboot'


class PaskReboot(PaskModule):
    def __init__(self, name, module_args):
        super(PaskReboot, self).__init__(name, module_args)

    @try_except
    def run(self):
        if self.module.params['verify'] == "yes":
            data = dict()
            self.resp = self.post(self.url, data)


def main():
    reboot = PaskReboot(name, module_args)
    reboot.set_param()
    reboot.run()
    reboot.set_result()


if __name__ == '__main__':
    main()
