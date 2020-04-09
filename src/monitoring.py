#!/usr/bin/python

import os
import sys
import time
import subprocess


def category():
    print('-'*94)
    print('|{:^30}|{:^30}|{:^30}|'.format('IP Address', 'MAC Address', 'Hostname'))
    print('-'*94)


def main():
    category()

    device = subprocess.check_output('./device.sh', shell=True)
    device_info = device.split('\n')[:-1]

    for dev in device_info:
        # [IP Address, MAC Address, Hostname]
        info = dev.split()
        print('|{:^30}|{:^30}|{:^30}|'.format(info[0], info[1], info[2]))
    print('-'*94 + '\n')

    while True:
        device = subprocess.check_output('./device.sh', shell=True)
        device_added = device.split('\n')[:-1]

        if sorted(device_added) != sorted(device_info):
            os.system('clear')

            category()

            for dev in device_added:
                info = dev.split()
                print('|{:^30}|{:^30}|{:^30}|'.format(info[0], info[1], info[2]))
            print('-'*94)

        device_info = device_added


if __name__ == "__main__":
    os.system('clear')

    main()
