#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Piolink.Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: pask_snmp
short_description: Configuring SNMP setting
description:
    - You can configure SNMP setting of the PAS-K.
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
    trap:
        description:
            - Enter the trap information
        type: dict

        suboptions:
            host:
                description:
                    - Enter the trap host information.
                type: list
                elements: dict

                suboptions:
                    ip:
                        description:
                            - Enter the ip address of the trap host.
                        required: true
                        type: str
                    version:
                        description:
                            - Enter the trap version.
                            - The value should be '1', '2c' or '3'.
                        type: str
                    community:
                        description:
                            - Enter the snmp community for snmp version '1' or '2c'.
                        type: str
                    des_passwd:
                        description:
                            - Enter the DES password for snmp version '3'.
                        type: str
                    md5_passwd:
                        description:
                            - Enter the MD5 password for snmp version '3'.
                        type: str
                    sha_passwd:
                        description:
                            - Enter the SHA password for snmp version '3'.
                        type: str
                    sha256_passwd:
                        description:
                            - Enter the SHA256 password for snmp version '3'.
                        type: str
                    aes_passwd:
                        description:
                            - Enter the AES passowrd for snmp version '3'.
                        type: str
                    engine_id:
                        description:
                            - Enter the Engine id of trap host for snmp version '3'.
                        type: str
                    user:
                        description:
                            - Enter the name of the snmp user for version '3'.
                        type: str
            cold_start:
                description:
                    - Enter whether to send trap when snmp enable.
                    - The value should be 'enable' or 'disable'.
                type: str
            failover:
                description:
                    - Enter whether to send trap when failover occur.
                    - The value should be 'enable' or 'disable'.
                type: str
            fan:
                description:
                    - Enter whether to send trap when cooling fan of PAS-K is shutdown.
                    - The value should be 'enable' or 'diable'.
                type: str
            health_check:
                description:
                    - Enter whether to send trap when health-check's result is changed
                    - The value should be 'enable' or 'disable'.
                type: str
            link_down:
                description:
                    - Enter whether to send trap when interface link down.
                    - The value should be 'enable' or 'disable'.
                type: str
            link_up:
                description:
                    - Enter whether to send trap when interface link up.
                    - The value should be 'enable' or 'disable'.
                type: str
            management_cpu:
                description:
                    - Enter whether to send trap when management cpu utilization exceeds the threshold.
                    - The value should be 'enable' or 'disable'.
                type: str
            management_memory:
                description:
                    - Enter whether to send trap when management memory utilization exceeds the threshold.
                    - The value should be 'enable' or 'disable'.
                type: str
            packet_cpu:
                description:
                    - Enter whether to send trapwhen packet processor cpu utilization exceeds the threshold.
                    - The value should be 'enable' or 'disable'.
                type: str
            packet_memory:
                description:
                    - Enter whether to send trap when packet processor memory utilization exceeds the threshold.
                    - The value should be 'enable' or 'disable'.
                type: str
            power:
                description:
                    - Enter whether to send trap when PAS-K power on or power off.
                    - The value should be 'enable' or 'disable'.
                type: str
            temperature:
                description:
                    - Enter whether to send trap when temperature exceeds the threshold.
                    - The value should be 'enable' or 'disable'.
                type: str

    community:
        description:
            - Enter the snmp community information.
        type: list
        elements: dict

        suboptions:
            name:
                description:
                    - Enther the name of the commnunity for snmp version '1' or '2c'.
                required: true
                type: str
            policy:
                description:
                    - Enter the policy of the commnunity.
                    - The value should be 'read-only' or 'read-write'.
                type: str
            limit_oid:
                description:
                    - Enter the oid accessible by using the community.
                type: str
    user:
        description:
            - Enter the user information for snmp version '3'.
        type: list
        elements: dict

        suboptions:
            name:
                description:
                    - Enter the snmp user name.
                required: true
                type: str
            des_passwd:
                description:
                    - Enter the DES password.
                type: str
            md5_passwd:
                description:
                    - Enter the MD5 password.
                type: str
            sha_passwd:
                description:
                    - Enter the SHA passowrd.
                type: str
            sha256_passwd:
                description:
                    - Enter the SHA256 passowrd.
                type: str
            aes_passwd:
                description:
                    - Enter the AES passowrd.
                type: str

    system:
        description:
            - Enter the PAS-K information for snmp.
        type: dict

        suboptions:
            name:
                description:
                    - Enter the name of the PAS-K.
                type: str
            contact:
                description:
                    - Enter the contact information.
                    - ex) email, telephone.
                type: str
            location:
                description:
                    - Enter the location of the PAS-K.
                type: str
    status:
        description:
            - Enter whether to use snmp.
            - The value should be 'enable' or 'disable'.
        type: str
    load_timeout:
        description:
            - Enter the load-timeout for snmp.
        type: str

requirements:
    - requests
'''

EXAMPLES = r'''
---
- name: SNMP Test
  hosts: all
  connection: local
  collections:
  - piolink_yhoh.pask_test

  tasks:
  - name: Create snmp
    pask_snmp:
      prest_ip: "{{ansible_host}}"
      prest_port: "{{ansible_port}}"
      user_id: "{{user_id}}"
      user_pw: "{{user_pw}}"
      status: "enable"
      load_timeout: "65535"
      system:
        name: "Piolink"
        contact: "admin@piolink.com"
        location: "Korea"
      community:
        - { name: "piolink", policy: "read-write", limit_oid: "1.1.1.1" }
        - { name: "piolink2", policy: "read-only", limit_oid: "1.1.1.1" }
      user:
        - { name: "test1", sha_passwd: "tester123!@#"}
      trap:
        link_up: "enable"
        link_down: "disable"
        failover: "enable"
        fan: "enable"
        cold_start: "enable"
        host:
          - {ip: "2.2.2.2", version: "3", user: "piolink", engine_id: "800007E5804089071BC6D10A41", aes_passwd: "Admin123$", sha_passwd: "Admin123$"}
          - {ip: "3.3.3.3", version: "3", user: "piolink12", engine_id: "800007E5804089071BC6D10A41", aes_passwd: "Admin123$", sha_passwd: "Admin123$"}
'''

RETURN = r'''
#
'''

from ansible_collections.piolink_yhoh.pask_test.plugins.module_utils.pask_module import PaskModule,\
    make_module_args, try_except


passwd_params_str = [
    'des_passwd', 'md5_passwd', 'sha_passwd', 'sha256_passwd', 'aes_passwd'
]
passwd_args = dict()
for p in passwd_params_str:
    passwd_args[p] = dict(type='str', no_log=True)

trap_host_params_str = [
    'community', 'engine_id', 'version', 'user'
]
inner_trap_host_args = dict(
    ip=dict(type='str', required=True),
)
inner_trap_host_args.update(make_module_args(trap_host_params_str))
inner_trap_host_args.update(passwd_args)

trap_params = [
    'cold_start', 'failover', 'fan', 'health_check', 'link_down',
    'link_up', 'management_cpu', 'management_memory', 'packet_cpu',
    'packet_memory', 'power', 'temperature'
]
inner_trap_args = dict(
    host=dict(type='list', elements='dict', options=inner_trap_host_args),
)
inner_trap_args.update(make_module_args(trap_params))

inner_user_args = dict(
    name=dict(type='str', required=True),
)
inner_user_args.update(passwd_args)

community_params = ['policy', 'limit_oid']
inner_community_args = dict(
    name=dict(type='str', required=True),
)
inner_community_args.update(make_module_args(community_params))

system_params = ['name', 'contact', 'location']
inner_system_args = make_module_args(system_params)

outermost_param_str = ['status', 'load_timeout']
outermost_args = make_module_args(outermost_param_str)

module_args = dict(
    trap=dict(type='dict', options=inner_trap_args),
    community=dict(type='list', elements='dict', options=inner_community_args),
    user=dict(type='list', elements='dict', options=inner_user_args),
    system=dict(type='dict', options=inner_system_args),
)
module_args.update(outermost_args)

name = 'snmp'


class PaskSnmp(PaskModule):
    def __init__(self, name, module_args):
        super(PaskSnmp, self).__init__(name, module_args)

    @try_except
    def run(self):
        data = self.make_data(self.module.params, include_inner=True)
        self.resp = self.put(self.url, data)


def main():
    snmp = PaskSnmp(name, module_args)
    snmp.set_param()
    snmp.run()
    snmp.set_result()


if __name__ == '__main__':
    main()
