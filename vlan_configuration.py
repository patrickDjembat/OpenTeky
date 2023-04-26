#! /usr/bin/env python3

#--- Function to get the Vlan and the name of the vlan
def get_commands(vlan, name):
    commands = []
    commands.append(f'vlan {vlan}')
    commands.append(f'name {name}')
    return commands

#--- Function for Theorically pushing the commands to the device.
#--- For now this function just push to the screen.
def push_commands(device, commands):
    print(f'Connecting to device: {device}')
    for cmd in commands:
        print(f'Sending command: {cmd}')

#--- Creating a list of devices
devices = ['switch1', 'switch2', 'switch3']

#--- List of VLANs to add as well as the Vlan names
vlans = [{'id': '10', 'name': 'USERS'}, {'id': '20', 'name': 'VOICE'},
{'id': '30', 'name': 'WLAN'}]

for vlan in vlans:
    vid = vlan.get('id')
    name = vlan.get('name')
    print(f'CONFIGURING VLAN: {vid}')
    commands = get_commands(vid, name)
    for device in devices:
        push_commands(device, commands)
        print()