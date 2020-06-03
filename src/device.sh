#!/bin/sh

# refer to show_wifi_client.sh of OpenWrt
# show IP, MAC address and hostname info for all connected Wi-Fi devices

# Extract IP Address, HW Address of ARP Table
arp_table=`cat /proc/net/arp | cut -f 1,2,12-15,21-23 -s -d" "`

mac_list=""
# list all wireless network interfaces (for MAC80211 driver)
for interface in `iw dev | grep Interface | cut -f 2 -s -d" "`; do
  # for each interface, get mac addresses of connected stations/clients
  mac=`iw dev $interface station dump | grep Station | cut -f 2 -s -d" "`
  mac_list="$mac_list $mac"
done

# for each mac address in that list
for mac in $mac_list; do
  arp_ip=`echo "$arp_table" | grep $mac | awk '{print $1}'`  
  arp_ip_cnt=`echo "$arp_ip" | wc -l`
  
  arp_invalid_cnt=`echo "$arp_table" | grep $mac | awk '{print $2}' | grep 0x0 | wc -l`
  arp_valid_cnt=`expr $arp_ip_cnt - $arp_invalid_cnt`

  for ip in $arp_ip; do
    dhcp_host=`cat /tmp/dhcp.leases | cut -f 2,3,4 -s -d" " | grep $ip | awk '{print $3}'`
    if [ -z "$dhcp_host" ]; then
      continue
    fi

    if [ $arp_valid_cnt -lt 2 ]; then
      # show wifi client of normal state
      echo -e "$ip\t$mac\t$dhcp_host\t-"
    else
      # show wifi client of abnormal state
      dhcp_mac=`cat /tmp/dhcp.leases | cut -f 2,3 -s -d" " | grep $ip | awk '{print $1}'`
      if [ -z "$dhcp_mac" ]; then
        continue
      fi

      if echo $mac_list | grep -q $dhcp_mac; then
        if [ "$mac" == "$dhcp_mac" ]; then
          # show wifi client of attacker
          echo -e "$ip\t$mac\t$dhcp_host\tHOST"
        else
          # show wifi client of victim
          echo -e "$ip\t$mac\t$dhcp_host\tVICTIM"
        fi
      else
        # show wifi client of vm
        echo -e "$ip\t$mac\t$dhcp_host\tVM"
      fi
    fi
  done
done
