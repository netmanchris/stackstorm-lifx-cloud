# LIFX Cloud Integration Pack
This pack allows you to integrate with
LIFX Light Bulbs using the LIFX cloud API. A developer account and 
token is required for the usage of this pack.

For Documentation on the LIFX APIs see https://api.developer.lifx.com/

This pack uses the pifx library for all communication to the LIFX cloud API
https://github.com/cydrobolt/pifx

Thanks to @cydrobolt for the great work. I don't know them. But appreciate their work.


## Configuration

Please use the following command to configure authentication of this pack

```
st2 pack config lifxcloud
```


**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`


## Actions

Actions are defined in two groups:

### Individual actions: GET, POST, PUT with under bar will precede each individual action
* ``get_alarms``
* ``get_switches``
* ``get_events``
* ``post_fit``

### Orquestra Workflows: will not
* ``sendsnow``
* ``performfit``
* ``getswitches``
* ``getfabric_for_fit``
