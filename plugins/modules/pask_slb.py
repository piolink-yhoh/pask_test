#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Piolink.Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: pask_slb
short_description: Configuring SLB setting
description:
    - You can configure SLB setting of the PAS-K.
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
            - Enter the service name.
        required: true
        type: str
    lb_method:
        description:
            - Enter the lb-method of the slb service.
            - The value should be 'dp', 'lc', 'lc-ss', 'lc-total', 'rr', 'sh', 'sh-port', 'srh', 'swrr', 'wlc', 'wlc-ss', 'wlc-total', 'wrr' or 'wsh'
        type: str
    vip:
        description:
            - Enter virtual IP address, protocol and port number.
        type: list
        elements: dict

        suboptions:
            ip:
                description:
                    - Enter the virtual IP address of the slb service.
                required: true
                type: str
            protocol:
                description:
                    - Enter the protocol and port number.
                type: dict

                suboptions:
                    protocol:
                        description:
                            - Enter the protocol of the slb service.
                        required: true
                        type: str
                    vport:
                        description:
                            - Enter the port number of the slb service.
                        type: str
    real:
        description:
            - Enter the real server information for the slb service.
        type: list
        elements: dict

        suboptions:
            id:
                description:
                    - Enter the real server id.
                required: true
                type: str
            rport:
                description:
                    - Enter the real server port number.
                type: str
            status:
                description:
                    - Enter whether to use real server option.
                    - The value should be 'enable' or 'disable'.
                type: str
            graceful_shutdown:
                description:
                    - Enter whether to use graceful shutdown option of the real server.
                    - The value should be 'enable' or 'disable'.
                type: str
    sticky:
        description:
            - Enter the sticky information for slb server.
        type: dict

        suboptions:
            time:
                description:
                    - Enter the sticky timeout.
                type: str
            source_subnet:
                description:
                    - Enter the subnet source ip address to apply persistent connection.
                type: str
    health_check:
        description:
            - Enter the health-check id.
        type: list
        elements: str
    slow_start:
        description:
            - Enter the slow-start information.
        type: dict

        suboptions:
            rate:
                description:
                    - Enter the slow-start rate.
                    - If you enter 'lc-ss' or 'wlc-ss' as a lb-method, you can set this value.
                type: str
            timer:
                description:
                    - Enter the slow-start timer.
                    - If you enter 'lc-ss' or 'wlc-ss' as a lb-method, you can set this value.
                type: str
    dynamic_proximity:
        description:
            - Enter the information of the dynamic-proximity setting.
        type: dict

        suboptions:
            name:
                description:
                    - Enter the name of the dynamic-proximity you created in advance
                    - If you enter 'dp' as a lb-method, you can set this value.
                required: true
                type: str
            ratio:
                description:
                    - Enter the ratio of dynamic-proximity.
                    - If you enter 'dp' as a lb-method, you can set this value.
                type: str
    session_timeout:
        description:
            - Enter the session timeout information.
            - If you enter 'service' as a session-timeout-mode, you can set theses values.
        type: dict

        suboptions:
            generic:
                description:
                    - If you want to set session timeout other than ICMP, TCP, and UDP sessions, you can set this value.
                type: str
            icmp:
                description:
                    - If you want to set session timeout of ICMP, you can set this value.
                type: str
            udp_stream:
                description:
                    - If you want to set session timeout of udp-stream, you can set this value.
                type: str
            udp:
                description:
                    - If you want to set session timeout of udp, you can set this value.
                type: str
            tcp_syn_sent:
                description:
                    - If you want to set session timeout of TCP in the'TCP-SYN-SENT' state, you can set this value.
                type: str
            tcp_syn_recv:
                description:
                    - If you want to set session timeout of TCP in the'TCP-SYN-RECV' state, you can set this value.
                type: str
            tcp_established:
                description:
                    - If you want to set session timeout of TCP in the'TCP-ESTABLISHED' state, you can set this value.
                type: str
            tcp_fin_wait:
                description:
                    - If you want to set session timeout of TCP in the'TCP-FIN-WAIT' state, you can set this value.
                type: str
            tcp_close_wait:
                description:
                    - If you want to set session timeout of TCP in the'TCP-CLOSE-WAIT' state, you can set this value.
                type: str
            tcp_last_ack:
                description:
                    - If you want to set session timeout of TCP in the'TCP-LAST-ACK' state, you can set this value.
                type: str
            tcp_wait:
                description:
                    - If you want to set session timeout of TCP in the'TCP-WAIT' state, you can set this value.
                type: str
            tcp_close:
                description:
                    - If you want to set session timeout of TCP in the'CLOSE' state, you can set this value.
                type: str
            tcp_unassured:
                description:
                    - If you want to set session timeout of TCP in the'UNASSURED' state, you can set this value.
                type: str
    filter:
        description:
            - Enter filter information for slb service.
        type: list
        elements: dict

        suboptions:
            id:
                description:
                    - Enter the filter id.
                required: true
                type: str
            type:
                description:
                    - Enter type of the filter.
                    - The value should be 'include' or 'exclude'.
                type: str
            protocol:
                description:
                    - Enter the protocol to be used as the filtering condition.
                    - The value should be 'tcp', 'udp', 'icmp' or 'all'.
                type: str
            dip:
                description:
                    - Enter the destination ip address and the number of netmask bits to be used as the filtering condition.
                type: str
            dport:
                description:
                    - Enter the destination port number to be used as the filtering condition.
                type: str
            sip:
                description:
                    - Enter the source ip address and the number of netmask bits to  be used as the filtering condition.
                type: str
            sport:
                description:
                    - Enter the source port number to be used as the filtering condition.
                type: str
            status:
                description:
                    - Enter whether to use filter for slb.
                    - The value should be 'enable' or 'disable'.
                type: str
    priority:
        description:
            - Enter the priority of the slb service.
        type: str
    nat_mode:
        description:
            - Enter the nat mode of the slb service.
            - The value should be 'both-nat', 'dnat', 'dsr', 'l3dsr-iptunnel' or 'lan-to-lan'
        type: str
    lan_to_lan:
        description:
            - Enter the IP band of servers acting as clients in the LAN area.
            - If you enter 'lan-to-lan' as a nat-mode, you can set this value.
        type: str
    session_sync:
        description:
            - Enter how to use session-sync.
            - The value should be 'all', 'none' or 'persistence'.
        type: str
    fail_skip:
        description:
            - Enter how to use fail-skip.
            - The value should be 'all', 'inact' or 'none'.
        type: str
    backup:
        description:
            - Enter the backup service of the slb service.
        type: str
    keep_backup:
        description:
            - Enter backup information.
        type: dict

        suboptions:
            service:
                description:
                    - Enter how to handle the session of the backup service, When the master real service becomes operational again.
                    - The value should be 'enable' or 'disable'.
                type: str
            real:
                description:
                    - Enter how to handle the session of the backup real server, When the master real server becomes operational again.
                    - The value should be 'enable' or 'disable'.
                type: str
    snatip:
        description:
            - Enter source nat ip address.
            - If you enter 'lan-to-lan' as a nat-mode, you can set this value.
        type: str
    passive_health_check:
        description:
            - Enter the passive-health-check id.
        type: list
        elements: str
    session_timeout_mode:
        description:
            - Enter the session-timeout-mode.
            - If you want to apply this value only to slb server, you should enter 'service'
            - Otherwise you can set 'global'.
        type: str
    session_reset:
        description:
            - Enter how to finish session when the real server is in 'INACT' state.
            - The value should be 'active', 'active-timeout', 'none', 'passive', 'passive-timeout' or 'timeout'.
        type: str
    active_nodest:
        description:
            - Enter whether to send RST packet to client when all real server is in 'INACT' state.
            - The value should be 'enable' or 'disable'.
        type: str
    status:
        description:
            - Enter whether to use the slb service.
            - The value should be 'enable' or 'disable'.
        type: str
    state:
        description:
            - Enter the status of this configuration.
            - If you want to delete this PAS-K configuration, enter 'absent',
            - otherwise, you can enter present or you don't have to do enter anything.
        type: str

requirements:
    - requests
'''

EXAMPLES = r'''
---
- name: Create slb Test
  hosts: all
  connection: local
  collections:
  - piolink_yhoh.pask_test

  tasks:
  - name: Create slb
    pask_slb:
      prest_ip: "{{ansible_host}}"
      prest_port: "{{ansible_port}}"
      user_id: "{{user_id}}"
      user_pw: "{{user_pw}}"
      name: "slb_test"
      vip:
          - { ip: "172.118.10.111", protocol: { protocol: "icmp", vport: "1231" }}
          - { ip: "172.118.10.122" }
      priority: "25"
      nat_mode: "dnat"
      lb_method: "wlc"
      real:
          - { id: "10", rport: "5512", status: "enable", graceful_shutdown: "disable" }
          - { id: "14" }
      health_check:
          - "100"
          - "200"
      slow_start:
          rate: "7"
          timer: "444"
      sticky:
          time: "4121"
          source_subnet: "255.255.255.0"
      session_sync: "persistence"
      fail_skip: "inact"
      keep_backup:
          service: "disable"
          real: "disable"
      status: "disable"
      state: "present"

  - name: Delete slb
    pask_slb:
        prest_ip: "{{ansible_host}}"
        prest_port: "{{ansible_port}}"
        user_id: "{{user_id}}"
        user_pw: "{{user_pw}}"
        name: "slb_test"
        state: "absent"
'''

RETURN = r'''
#
'''

from ansible_collections.piolink_yhoh.pask_test.plugins.module_utils.pask_module import PaskModule,\
    make_module_args, try_except
import os


# make vip args
protocol_inner_args = dict(
    protocol=dict(type='str', required=True),
    vport=dict(type='str')
)

vip_inner_args = dict(
    ip=dict(type='str', required=True),
    protocol=dict(type='dict', options=protocol_inner_args)
)

# real inner args
real_inner_args = dict(
    id=dict(type='str', required=True)
)
real_inner_param = [
    'rport', 'status', 'graceful_shutdown'
]
real_inner_args.update(make_module_args(real_inner_param))

slow_start_inner_args = dict(
    rate=dict(type='str'),
    timer=dict(type='str')
)

# sticky param
sticky_inner_param = [
    'time', 'source_subnet'
]
sticky_inner_args = make_module_args(sticky_inner_param)

# make dynamic_proximity_args
dynamic_proximity_inner_args = dict(
    name=dict(type='str', required=True),
    ratio=dict(type='str')
)

# session_timeout inner_args
session_timeout_params = [
    'generic', 'icmp', 'udp', 'udp_stream', 'tcp_syn_sent', 'tcp_syn_recv',
    'tcp_established', 'tcp_fin_wait', 'tcp_close_wait', 'tcp_last_ack',
    'tcp_wait', 'tcp_close', 'tcp_unassured'
]
session_timeout_inner_args = make_module_args(session_timeout_params)

# make filter args
filter_inner_args = dict(
    id=dict(type='str', required=True)
)
filter_param = [
    'dip', 'dport', 'protocol', 'sip', 'sport', 'status', 'type'
]
filter_inner_args.update(make_module_args(filter_param))

# make keep-backup args
keep_backup_inner_args = dict(
    service=dict(type='str'),
    real=dict(type='str')
)

# make outermost of module_args
module_args = dict(
    name=dict(type='str', required=True),
    vip=dict(type='list', elements='dict', options=vip_inner_args),
    real=dict(type='list', elements='dict', options=real_inner_args),
    sticky=dict(type='dict', options=sticky_inner_args),
    health_check=dict(type='list', elements='str'),
    passive_health_check=dict(type='list', elements='str'),
    slow_start=dict(type='dict', options=slow_start_inner_args),
    dynamic_proximity=dict(type='dict', options=dynamic_proximity_inner_args),
    session_timeout=dict(type='dict', options=session_timeout_inner_args),
    filter=dict(type='list', elements='dict', options=filter_inner_args),
    keep_backup=dict(type='dict', options=keep_backup_inner_args)
)

str_param_list = [
    'priority', 'nat_mode', 'lan_to_lan', 'lb_method', 'session_sync',
    'fail_skip', 'backup', 'status', 'snatip', 'state', 'session_timeout_mode',
    'session_reset', 'active_nodest'
]
module_args.update(make_module_args(str_param_list))

name = 'slb'


class PaskSlb(PaskModule):
    def __init__(self, name, module_args):
        super(PaskSlb, self).__init__(name, module_args)

    @try_except
    def run(self):
        data = dict()
        if self.module.params['state'] == "absent":
            data[name] = {'name': self.module.params['name']}
            self.ok_error_msg['delete'] = ['EntryDoesNotExist']
            self.resp = self.delete(self.url, data)
        else:
            data = self.make_data(self.module.params, include_inner=True)
            filter_data = self.make_filter_data(data)
            data['filter'] = filter_data
            url = os.path.join(self.url, self.module.params['name'])
            self.resp = self.put(url, data)

    def make_filter_data(self, data):
        # module do not have filter data in playbook script
        vip_filter = self.make_filter_by_vip(data['vip'])

        if data.get('filter') is None:
            for _id in range(len(vip_filter)):
                vip_filter[_id]['id'] = str(_id + 1)
            return vip_filter

        # module have filter data in playbook script
        filter_data = list()
        used_filter_id = list()
        for param in data['filter']:
            used_filter_id.append(param['id'])

        f_compare_list = [
            'type', 'dip', 'sip', 'protocol', 'dport'
        ]

        append = False
        for vf in vip_filter:
            for df in data['filter']:
                for p in f_compare_list:
                    if vf.get(p) is None:
                        continue
                    if df.get(p) is None:
                        append = True
                    if vf[p] != df[p]:
                        append = True
            if append:
                for _id in range(1, 255):
                    if str(_id) not in used_filter_id:
                        vf['id'] = str(_id)
                        filter_data.append(vf)
                        used_filter_id.append(str(_id))
                        break

        return filter_data + data['filter']

    def make_filter_by_vip(self, vips):
        # make filter without id
        filter_list = list()

        for vip in vips:
            f_made_by_vip = {
                'type': 'include',
                'sip': '0.0.0.0/0',
                'protocol': 'all',
                'status': 'enable'
            }
            f_made_by_vip['dip'] = vip['ip'] + "/32"

            if vip.get('protocol') is not None:
                if vip['protocol'].get('vport') is not None:
                    f_made_by_vip['dport'] = vip['protocol'].get('vport')
                if vip['protocol'].get('protocol') is not None:
                    f_made_by_vip['protocol'] = vip['protocol'].get('protocol')
            filter_list.append(f_made_by_vip)
        return filter_list


def main():
    real = PaskSlb(name, module_args)
    real.set_param()
    real.run()
    real.set_result()


if __name__ == '__main__':
    main()
