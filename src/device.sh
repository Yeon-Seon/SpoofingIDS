#!/bin/sh

# refer to show_wifi_client.sh of OpenWrt
# show IP, MAC address and hostname info for all connected Wi-Fi devices
# echo "# All connected wifi devices, with IP address"
# echo "# hostname (if available), and MAC address"
# echo "# IP address, MAC address, hostname"

# list all wireless network interfaces (for MAC80211 driver)
for interface in `iw dev | grep Interface | cut -f 2 -s -d" "`
do
  # for each interface, get mac addresses of connected stations/clients
  mac_list=`iw dev $interface station dump | grep Station | cut -f 2 -s -d" "`

  # for each mac address in that list
  for mac in $mac_list
  do
    # if a DHCP Lease has been given out by dnsmasq, save it
    ip=`cat /tmp/dhcp.leases | cut -f 2,3,4 -s -d" " | grep $mac | cut -f 2 -s -d" "`
    host=`cat /tmp/dhcp.leases | cut -f 2,3,4 -s -d" " | grep $mac | cut -f 3 -s -d" "`

    # show the mac address
    echo -e "$ip\t$mac\t$host"
  done
done
