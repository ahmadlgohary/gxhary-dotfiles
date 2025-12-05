#!/usr/bin/python
import os
from time import sleep

def wifi_icon(signal):
    signal = int(signal)
    if signal > 75:
        return "󰤨"
    elif signal > 50:
        return "󰤥"
    elif signal > 25:
        return "󰤢"
    else:
        return "󰤟"

def is_empty_string(input_string):
    return bool(input_string.strip())

def get_available_wifi_networks():
    wifi_list = os.popen('nmcli -t --fields "SECURITY,SSID,SIGNAL" device wifi list').read()
    return list(filter(is_empty_string, wifi_list.split("\n")))





def format_list_of_wifi_names(wifi_list):
    for i, wifi_network in enumerate(wifi_list):

        wifi_network=wifi_network.split(":")

        # skip networks with no ssid
        if not wifi_network[1]:
            wifi_list[i] = ""
            continue

        wifi_network[0] = "" if wifi_network[0] else  ""
        wifi_network[2] = wifi_icon(wifi_network[2])
        wifi_list[i] = " ".join(wifi_network)
    return "\n".join(list(filter(is_empty_string, wifi_list)))



def main():
    formatted_wifi_list=format_list_of_wifi_names(get_available_wifi_networks())
    with open(os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__))), "wifi_list"),"w") as f:
        f.write(formatted_wifi_list)

if __name__ == "__main__":
    main()
    sleep(30)
    main()

