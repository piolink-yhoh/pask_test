# -*- coding:utf-8 -*-

# Copyright: (c) 2020, Piolink Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import base64
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

from ansible.module_utils._text import to_bytes
from ansible.module_utils.basic import AnsibleModule, missing_required_lib


OP_GET = 0
OP_POST = 1
OP_PUT = 2
OP_DELETE = 3


class PrestApi(object):
    def __init__(self):
        self.headers = {'Authorization': '',
                        'Content-Type': ''}
        self.used_method = list()
        if not HAS_REQUESTS:
            AnsibleModule(argument_spec={}, check_invalid_arguments=False)\
                .fail_json(msg=missing_required_lib('requests'))

    def basic_auth(self, username, password):
        return "Basic %s" % base64.b64encode(to_bytes(
            "%s:%s" % (username, password), errors='surrogate_or_strict'))

    def set_headers(self, username, password):
        self.headers['Authorization'] = self.basic_auth(username, password)
        self.headers['Content-Type'] = 'application/json'

    def get(self, url):
        self.used_method.append('get')
        return requests.get(url, headers=self.headers, verify=False)

    def post(self, url, data=None):
        self.used_method.append('post')
        if data is not None:
            return requests.post(url, headers=self.headers, json=data,
                                 verify=False)
        else:
            return requests.post(url, headers=self.headers, verify=False)

    def put(self, url, data=None):
        self.used_method.append('put')
        if data:
            return requests.put(url, headers=self.headers, json=data,
                                verify=False)
        else:
            return requests.put(url, headers=self.headers, verify=False)

    def delete(self, url, data=None):
        self.used_method.append('delete')
        if data:
            return requests.delete(url, headers=self.headers, json=data,
                                   verify=False)
        else:
            return requests.delete(url, headers=self.headers, verify=False)

    def is_exist(self, url, key):
        ret = self.get(os.path.join(url, key))
        if len(ret.text) > 2:
            return True
        else:
            return False