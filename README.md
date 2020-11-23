# Piolink PAS-K Ansible Collection
The Collection is the Piolink PAS-K Ansible Automation project.
It includes the modules that are able to configure PAS-K machine's settings.

# Installation
This collection is distributed via [ansible-galaxy](https://galaxy.ansible.com/), the installation steps are as follows:

1. Install or upgrade to Ansible 2.9+
2. Download this collection from galaxy: `ansible-galaxy collection install piolink.pask_ansible_collection`

# Requirements
* Ansible 2.9+ is required to support the newer Ansible Collections format
* requests module
* netaddr module

# Modules
The collection provides the following modules:

* `pask_dns` You can configure DNS setting of the PAS-K.
* `pask_health_check` You can configure health check setting of the PAS-K.
* `pask_hostname` You can configure hostname setting of the PAS-K.
* `pask_interface` You can configure interface setting of the PAS-K.
* `pask_ntp` You can configure NTP client setting of the PAS-K.
* `pask_prest` You can configure PAS-K setting by using the PREST API.
* `pask_real`  You can configure real server setting of the PAS-K.
* `pask_reboot` You can reboot the PAS-K machine.
* `pask_reset` You can initalize the PAS-K settings.
* `pask_route` You can configure route setting of the PAS-K.
* `pask_slb` You can configure SLB setting of the PAS-K.
* `pask_snmp` You can configure SNMP setting of the PAS-K.
* `pask_user` You can configure user setting of the PAS-K.
* `pask_vlan` You can configure vlan setting of the PAS-K.
* `pask_writememory` You can save PAS-K setting.

# Usage
The following example is used to configure DNS setting of the PAS-k.

playbook example(pask_dns.yml):
```yaml
---
- name: Dns Test
  hosts: all
  connection: local
  collections:
  - piolink_yhoh.pask_test

  tasks:
  - name: create dns ip
    pask_dns:
      prest_ip: "{{ansible_host}}"
      prest_port: "{{ansible_port}}"
      user_id: "{{user_id}}"
      user_pw: "{{user_pw}}"
      retry: "5"
      timeout: "10"
      id:
        - { id: "1", ip: "192.168.203.100" }
        - { id: "2", ip: "8.8.8.8" }
```
Run the playbook command:
```bash
ansible-playbook pask_dns.yml
```
