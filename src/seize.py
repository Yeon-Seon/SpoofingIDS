#!/usr/bin/python

import os
import sys
import time
import subprocess


class SZ:
    def __init__(self):
        self.connect_device = list()
        self.continue_device = list()
        self.client = dict()

    def wifi_device(self):
        data = subprocess.check_output('./device.sh', shell=True)
        self.connect_device = data.split('\n')[:-1]

        if sorted(self.connect_device) != sorted(self.continue_device):
            device = list(set(self.connect_device) - set(self.continue_device))
            flag = True

            if not device:
                device = list(set(self.continue_device) - set(self.connect_device))
                flag = False

            self.parse(device, flag)

    def parse(self, device, flag):
        for dev in device:
            data = dev.split()

            if flag is True:
                ip = data[0]
                mac = data[1]
                host = data[2]
                connect_time = time.strftime('%Y-%m-%d %H:%M:%S')
                start_time = time.time()

                self.client[mac] = [ip, host, connect_time, start_time]
            else:
                mac = data[1]
                del self.client[mac]

        self.continue_device = self.connect_device

    def reset(self):
        os.system('clear')

    def frame(self):
        print('-'*136)
        print('|{:^25}|{:^25}|{:^25}|{:^25}|{:^30}|'.format('IP Address', 'MAC Address', 'Hostname', 'Connection Time', 'Continuous Time (second)'))
        print('-'*136)

    def show(self):
        for key, value in self.client.items():
            continuous_time = int(time.time() - value[3])
            print('|{:^25}|{:^25}|{:^25}|{:^25}|{:^30}|'.format(value[0], key, value[1], value[2], continuous_time))
        print('-'*136 + '\n')

    def screen(self):
        self.wifi_device()
        self.reset()
        self.frame()
        self.show()

    def monitor(self):
        while True:
            self.screen()

            print('Number of connected devices : {}'.format(len(self.client)))

- seize.py 72/72 100%
