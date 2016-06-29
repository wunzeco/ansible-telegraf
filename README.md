telegraf
==============

Ansible role to install and configure Telegraf.


## Example

```
- hosts: myhost

  vars:
    telegraf_version: "0.13.0-1"
    
  roles:
    - wunzeco.telegraf
```

> **Note:** 
>    example variables for configuring input and output plugins, see
>    `test/input-plugins-vars.yml` and `test/output-plugins-vars.yml` respectively


## Testing

To run this role's integration tests

```
kitchen test
```


## Dependencies

none

