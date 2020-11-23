#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Piolink.Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: pask_prest
short_description: Configuring PAS-K setting by using the PREST API.
description:
    - You can configure PAS-K setting by using the PREST API.
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
    uri:
        description:
            - Enter the uri to use PREST API.
        required: true
        type: str
    data:
        description:
            - Enter the body data to use PREST API.
            - The data must be in json format.
        type: str
    method:
        description:
            - Enter the method of PREST API.
            - The value should be 'get', 'post', 'put' or 'delete'.
        type: str

requirements:
    - requests
'''

EXAMPLES = r'''
---
- name: Prest Test
  hosts: all
  connection: local
  collections:
  - piolink_yhoh.pask_test

  tasks:
  - name: Configure terminal setting
    pask_prest :
      prest_ip: "{{ansible_host}}"
      prest_port: "{{ansible_port}}"
      user_id: "{{user_id}}"
      user_pw: "{{user_pw}}"
      uri: "/prestapi/v2/conf/terminal"
      data: >
            {
                "timeout" : "60",
                "length" : "80"
            }
      method: "put"
'''

RETURN = r'''
#
'''

import json
from ansible_collections.piolink_yhoh.pask_test.plugins.module_utils.\
    pask_module import PaskModule


module_args = dict(
    uri=dict(type='str', required=True),
    data=dict(type='str'),
    method=dict(type='str')
)

name = 'prest'


class PaskPrest(PaskModule):
    def __init__(self, name, module_args):
        super(PaskPrest, self).__init__(name, module_args)

    def run(self):
        resp = None
        rest_method = ['get', 'post', 'put', 'delete']
        if self.module.params['method'] not in rest_method:
            return self.result
        url = 'https://{0}:{1}{2}'.format(self.module.params['prest_ip'],
                                          self.module.params['prest_port'],
                                          self.module.params['uri'])
        if self.module.params['data'] is not None:
            data = json.loads(self.module.params['data'])

        if self.module.params['method'] == 'get':
            resp = self.get(url)
        elif self.module.params['method'] == 'post':
            resp = self.post(url, data)
        elif self.module.params['method'] == 'put':
            resp = self.put(url, data)
        elif self.module.params['method'] == 'delete':
            resp = self.delete(url, data)

        if resp is not None:
            self.resp = resp


def main():
    prest = PaskPrest(name, module_args)
    prest.set_param()
    prest.run()
    prest.set_result()


if __name__ == '__main__':
    main()
