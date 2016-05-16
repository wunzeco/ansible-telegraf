telegraf
==============

Ansible role to install and configure Telegraf.


## Example

```
- hosts: myhost

  vars:
    
  roles:
    - wunzeco.telegraf
```


## Dependencies

none

## ToDo
- template telegraf.conf
- template /etc/default/telegraf
- template or copy /etc/logrotate.d/telegraf
