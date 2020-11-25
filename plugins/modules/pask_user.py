#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Piolink.Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: pask_user
short_description: Configuring user setting
description:
    - You can congigure user setting of the PAS-K.
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
    name:
        description:
            - Enter the name of the user.
        required: true
        type: str
    password:
        description:
            - Enter the password of the user.
        type: str
    config_password:
        description:
            - Enter the password of the superuser.
            - If you want to enter configuration mode, you need the password.
        type: str
    level:
        description:
            - Enter the level of the user.
            - The value should be 'superuser' or 'user'.
        type: str
    description:
        description:
            - Enter the description of the user.
        type: str
    log:
        description:
            - Enter the access-right to access PAS-K's log.
            - The value should be 'enable' or 'disable'.
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
- name: User Test
  hosts: all
  connection: local
  collections:
  - piolink_yhoh.pask_test

  tasks:
  - name: Create User
    pask_user:
      prest_ip: "{{ansible_host}}"
      prest_port: "{{ansible_port}}"
      user_id: "{{user_id}}"
      user_pw: "{{user_pw}}"
      name: "piolink"
      description: "Piolink administrator"
      level: "user"
      log: "disable"
      password: "Admin123$"

  - name: Delete User
    pask_user:
      prest_ip: "{{ansible_host}}"
      prest_port: "{{ansible_port}}"
      user_id: "{{user_id}}"
      user_pw: "{{user_pw}}"
      name: "piolink"
      description: "Piolink administrator"
      level: "user"
      log: "disable"
      password: "Admin123$"
      state: "absent"
'''

RETURN = r'''
#
'''

from ansible_collections.piolink_yhoh.pask_test.plugins.module_utils.pask_module import PaskModule,\
    make_module_args, try_except
import os


outermost_param_str = [
    'description', 'level', 'log', 'state'
]
outermost_args = make_module_args(outermost_param_str)

password_args = dict(
    password=dict(type='str', no_log=True),
    config_password=dict(type='str', no_log=True)
)

module_args = dict(
    name=dict(type='str', required=True)
)
module_args.update(outermost_args)
module_args.update(password_args)

name = 'user'


class PaskUser(PaskModule):
    def __init__(self, name, module_args):
        super(PaskUser, self).__init__(name, module_args)

    @try_except
    def run(self):
        url = os.path.join(self.url, self.module.params['name'])
        if self.module.params['state'] == 'absent':
            self.resp = self.delete(url)
        else:
            data = self.make_data(self.module.params, include_inner=True)
            self.resp = self.put(url, data)


def main():
    user = PaskUser(name, module_args)
    user.set_param()
    user.run()
    user.set_result()


if __name__ == '__main__':
    main()
