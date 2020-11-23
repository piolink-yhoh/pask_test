#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Piolink.Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: pask_interface
short_description: Configuring interface setting
description:
    - You can configure interface setting of the PAS-K.
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
            - Enter the interface name.
        required: true
        type: str
    ip:
        description:
            - Enter the ipv4 information.
        type: dict

        suboptions:
            address:
                description:
                    - Enter the ipv4 address and net mask of the interface.
                required: true
                type: str
            broadcast:
                description:
                    - Enter the broadcast address of theinterface.
                type: str
            overlapped:
                description:
                    - Enter whether to use the ip address as a nat ip or virutal ip.
                    - If you want to set this value, you should enter 'on'
                type: str
    ip6:
        description:
            -  Enter the ipv6 information.
        type: dict

        suboptions:
            address:
                description:
                    - Enter the ipv6 address and net mask of the interface.
                required: true
                type: str
            broadcast:
                description:
                    - Enter the broadcast address of the interface.
                type: str
            adv_on_link:
                description:
                    - Enter the whether to use the ip address for on-link.
                    - The value should be 'enable' or 'disable'.
                type: str
            adv_autonomous:
                description:
                    - Enter the whether to use the ip address for autonomous address configuration.
                    - The value should be 'enable' or 'disable'.
                type: str
            adv_router_addr:
                description:
                    - If you want to set the network prefix instead of the interface address, enter 'enable'.
                    - Otherwise enter 'disable'.
                type: str
            adv_valid_lifetime:
                description:
                    - Enter the valid time of the prefix in seconds.
                type: str
            adv_preferred_lifetime:
                description:
                    - Set address autoconfiguration remain prefferred in seconds.
                type: str
    mtu:
        description:
            - Enter the mtu of the interface.
        type: str
    rpf:
        description:
            - Enter how to use rpf(Reverse Path Forwarding) function of the interface.
            - The value should be 'default', 'strict' or 'loose'.
        type: str
    status:
        description:
            - Enter the status of the interface.
            - The value should be 'up' or 'down'.
        type: str
    adv_send_advert:
        description:
            - Enter whether to use router advertisements and solicitations.
            - The value should be 'enable' or 'disable'.
        type: str
    adv_cur_hop_limit:
        description:
            - Enter the default hop count.
        type: str
    adv_default_lifetime:
        description:
            - Enter the lifetime in seconds.
        type: str
    adv_retrans_timer:
        description:
            - Enter the wait time in milliseconds.
        type: str
    adv_reachable_time:
        description:
            - Enter the reachability time in milliseconds.
        type: str
    max_rtr_adv_interval:
        description:
            - Enter the maximum time R/A in seconds.
        type: str
    min_rtr_adv_interval:
        description:
            - Enter the minimum time R/A in seconds.
        type: str
    state:
        description:
            - Enter the status of this configuration.
            - If you want to delete this PAS-K configuration, enter absent,
            - otherwise, you can enter present or you don't have to do enter anything.
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
  - name: create interface ip
    pask_interface:
      prest_ip: "{{ansible_host}}"
      prest_port: "{{ansible_port}}"
      user_id: "{{user_id}}"
      user_pw: "{{user_pw}}"
      name: "test_vlan"
      mtu: "750"
      status: "down"
      rpf: "loose"
      adv_cur_hop_limit: "100"
      adv_reachable_time: "5012"
      ip:
          address: "172.118.20.111/32"
          broadcast: "172.118.20.1"
          overlapped: "on"

  - name: delete interface ip
    pask_interface:
      prest_ip: "{{ansible_host}}"
      prest_port: "{{ansible_port}}"
      user_id: "{{user_id}}"
      user_pw: "{{user_pw}}"
      name: "test_vlan"
      mtu: "750"
      status: "down"
      rpf: "loose"
      state: "absent"
      ip:
          address: "172.118.20.111/32"
          broadcast: "172.118.20.1"
          overlapped: "on"
'''

RETURN = r'''
#
'''

from ansible_collections.piolink_yhoh.pask_test.plugins.module_utils.\
    pask_module import PaskModule, make_module_args, try_except
import os


inner_ip_args = dict(
    address=dict(type='str', required=True),
    broadcast=dict(type='str'),
    overlapped=dict(type='str')
)

inner_ip6_args = dict(
    address=dict(type='str', required=True),
)

inner_ip6_params_str = [
    'broadcast', 'adv_on_link', 'adv_autonomous', 'adv_router_addr',
    'adv_valid_lifetime', 'adv_preferred_lifetime',
]
inner_ip6_args.update(make_module_args(inner_ip6_params_str))


module_args = dict(
    name=dict(type='str', required=True),
    ip=dict(type='dict', options=inner_ip_args),
    ip6=dict(type='dict', options=inner_ip6_args),
)

outermost_param_str = [
    'mtu', 'rpf', 'status', 'state', 'adv_cur_hop_limit',
    'adv_default_lifetime', 'adv_reachable_time', 'adv_retrans_timer',
    'adv_send_advert', 'max_rtr_adv_interval', 'min_rtr_adv_interval',
]
module_args.update(make_module_args(outermost_param_str))

name = 'interface'


class PaskInterface(PaskModule):
    def __init__(self, name, module_args):
        super(PaskInterface, self).__init__(name, module_args)

    @try_except
    def run(self):
        data = self.make_data(self.module.params, include_inner=True)
        url = os.path.join(self.url, self.module.params['name'])
        if self.module_params['state'] == 'absent':
            self.ok_error_msg['delete'] = ['There is no']
            self.resp = self.delete(url, data)
        else:
            self.resp = self.put(url, data)


def main():
    interface = PaskInterface(name, module_args)
    interface.set_param()
    interface.run()
    interface.set_result()


if __name__ == '__main__':
    main()
