#!/usr/bin/python
import re
import os
import sys

battery_info= os.popen("acpi -b").read()
is_discharging = True if sys.argv[1] == "0" else False
battery_level = re.findall(r'[0-9]+(?=%)', battery_info)[0]

if is_discharging:
    battery_state = "Discharging"
    notification_message = f"{battery_level}% of battery remaining."
    notification_icon_name = "battery-discharging"
    notification_sound = "battery_discharging.mp3"
else:
    battery_state = "Charging"
    notification_message = f"{battery_level}% of battery charged."
    notification_icon_name = "battery-charging"
    notification_sound = "battery_charging.ogg"

SYSTEM_VARIABLES = [
    'export DISPLAY=:0',
    'export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"' ,
    'export XAUTHORITY=/home/gxhary/.Xauthority',
    'export XDG_RUNTIME_DIR="/run/user/1000"'
    ]

COMMANDS = [
        f'notify-send "{battery_state}" "{notification_message}" -h string:synchronous:battery_notif -u low -e -i "{notification_icon_name}" -t 5000 -r 9991',
        f"paplay {os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', notification_sound)}"
    ]
print(" && ".join(SYSTEM_VARIABLES + COMMANDS))
os.system(" && ".join(SYSTEM_VARIABLES + COMMANDS))
