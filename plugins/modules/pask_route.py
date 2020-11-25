#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Piolink.Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: pask_route
short_description: Configuring route setting
description:
    - You can configure route setting of the PAS-K.
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
    network:
        description:
            - Enter route information for static routing.
        type: list
        elements: dict

        suboptions:
            dest:
                description:
                    - Enter the destination ip address.
                required: true
                type: str
            interface:
                description:
                    - Enter the interface information for static routing.
                type: list
                elements: dict

                suboptions:
                    interface:
                        description:
                            - Enter the VLAN interface name to be routed through to reach the destination.
                        type: str
            gateway:
                description:
                    - Enter the gateway information for static routing.
                type: list
                elements: dict

                suboptions:
                    gateway:
                        description:
                            - Enter the gateway ip address to be routed through to reach the destination.
                        type: str
    default_gateway:
        description:
            - Enter the default-gateway information.
        type: list
        elements: dict

        suboptions:
            gateway:
                description:
                    - Enter the default gateway ip address.
                required: true
                type: str
            health_check:
                description:
                    - Enter health-check information for default-gateway.
                type: list
                elements: dict

                suboptions:
                    id:
                        description:
                            - Enter the health-check id for default-gateway.
                        required: true
                        type: str
            priority:
                description:
                    - Enter the priority of the default gateway.
                type: str

requirements:
    - requests
    - netaddr
'''

EXAMPLES = r'''
---
- name: Route Module Test
  connection: local
  hosts: targets
  collections:
  - piolink_yhoh.pask_test

  tasks:
  - name: Create route
    pask_route:
      prest_ip: "{{ansible_host}}"
      prest_port: "{{ansible_port}}"
      user_id: "{{user_id}}"
      user_pw: "{{user_pw}}"
      default_gateway:
          - {priority: "100", gateway: "192.168.214.1", health_check: {id: "1"}}
          - {priority: "5", gateway: "192.168.224.1", health_check: {id: "1"}}
      network:
          - { dest: "10.10.0.0/16",
              gateway: [
                {gateway: "10.10.10.1"},
              ],
            }
          - { dest: "10.20.0.0/16",
              interface: [
                  {interface: "v2933"},
                  {interface: "v2944"}
              ]
            }
'''

RETURN = r'''
#
'''

try:
    import netaddr
    HAS_NETADDR = True
except ImportError:
    HAS_NETADDR = False

import json
from ansible.module_utils.basic import missing_required_lib
from ansible_collections.piolink_yhoh.pask_test.plugins.module_utils.pask_module import PaskModule,\
    make_module_args, try_except

inner_interface_params = ['interface']
inner_interface_args = make_module_args(inner_interface_params)

inner_gateway_params = ['gateway']
inner_gateway_args = make_module_args(inner_gateway_params)

inner_network_args = dict(
    dest=dict(type='str', required=True),
    interface=dict(type='list', elements='dict', options=inner_interface_args),
    gateway=dict(type='list', elements='dict', options=inner_gateway_args)
)

inner_health_check_args = dict(
    id=dict(type='str', required=True)
)

inner_defaultgw_args = dict(
    priority=dict(type='str'),
    gateway=dict(type='str', required=True),
    health_check=dict(type='list', elements='dict',
                      options=inner_health_check_args)
)

module_args = dict(
    network=dict(type='list', elements='dict', options=inner_network_args),
    default_gateway=dict(type='list', elements='dict',
                         options=inner_defaultgw_args)
)

name = 'route'


class PaskRoute(PaskModule):
    def __init__(self, name, module_args):
        super(PaskRoute, self).__init__(name, module_args)

        if not HAS_NETADDR:
            self.module.fail_json(msg=missing_required_lib('netaddr'))

    @try_except
    def run(self):
        interface_url = self.url.replace(name, 'interface')
        resp = self.get(interface_url)
        resp_dict = json.loads(resp.text)

        if_list = self.get_if_and_ip(resp_dict['interface'])

        route_data = self.make_route_data_from_interface(if_list)

        data = self.make_data(self.module.params, include_inner=True)

        if data.get('network') is None:
            data['network'] = route_data
        else:
            data['network'].extend(route_data)

        self.resp = self.put(self.url, data)

    def get_if_and_ip(self, data):
        """
            return value example
        [
            {'interface': 'mgmt', 'ip': '192.168.214.145/24'},
            {'interface': 'v2933', 'ip': '10.10.10.100/24'},
            {'interface': 'v2933', 'ip': '10.10.10.100/28'}
        ]
        """
        if_list = list()
        for interface in data:
            if interface.get('ip') is None:
                continue

            if isinstance(interface['ip'], list):
                for ip in interface['ip']:
                    d = {
                        'ip': ip['address'],
                        'interface': interface['name']
                    }
                    if_list.append(d)
            else:
                d = {
                    'ip': interface['ip']['address'],
                    'interface': interface['name']
                }
                if_list.append(d)
        return if_list

    def make_route_data_from_interface(self, if_list):
        network = list()
        for _if in if_list:
            net = netaddr.IPNetwork(_if['ip'])
            dest = str(net.network) + "/" + str(net.prefixlen)
            d = {
                "dest": dest,
                "interface": {
                    "interface": _if['interface']
                }
            }
            network.append(d)
        return network


def main():
    route = PaskRoute(name, module_args)
    route.set_param()
    route.run()
    route.set_result()


if __name__ == '__main__':
    main()
