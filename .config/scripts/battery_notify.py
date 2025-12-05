#!/usr/bin/python
import re
import os
import json

SYSTEM_VARIABLES = 'export DISPLAY=:0 && export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus" &&'
WARNING_LEVEL = 20

battery_state = ""
notification_message = ""
notification_icon_name = ""
notification_sound = ""


try:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "battery_status.json"), "r") as f:
        battery_status = json.loads(f.read())
except:
    battery_status = {"battery_charged": False, "battery_empty": False}

battery_info= os.popen("acpi -b").read()
is_discharging = True if "Discharging" in battery_info else False
battery_level = int(re.findall(r'[0-9]+(?=%)', battery_info)[0])

if is_discharging and battery_status['battery_charged']:
    battery_status['battery_charged'] = False

elif not is_discharging and battery_status['battery_empty']:
    battery_status['battery_empty'] = False

if battery_level > 99 and not is_discharging and not battery_status['battery_charged']:
    battery_status['battery_charged'] = True
    battery_state = "Battery Charged"
    notification_message = "Battery is fully charged."
    notification_icon_name = "battery"
    notification_sound = "battery_charging.ogg"

elif battery_level <= WARNING_LEVEL and is_discharging and not battery_status['battery_empty']:
    battery_status['battery_empty'] = True
    battery_state = "Low Battery"
    notification_message = f"{battery_level}% of battery remaining."
    notification_icon_name = "battery-alert"
    notification_sound = "battery_low.ogg"



SYSTEM_VARIABLES = [
    'export DISPLAY=:0',
    'export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"' ,
    'export XAUTHORITY=/home/gxhary/.Xauthority',
    'export XDG_RUNTIME_DIR="/run/user/1000"'
    ]

COMMANDS = [
        f'notify-send "{battery_state}" "{notification_message}" -h string:synchronous:battery_notif -u critical -e -i "{notification_icon_name}" -r 9991',
        f"paplay {os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', notification_sound)}"
    ]

if battery_state:
    os.system(" && ".join(SYSTEM_VARIABLES + COMMANDS))



with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "battery_status.json"), "w") as f:
    f.write(json.dumps(battery_status, indent = 4))
