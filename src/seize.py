#!/usr/bin/python3

import os
import sys
import time
import subprocess


class SZ:
    def __init__(self):
        self.victim = ''
        self.state = False

        self.connect_device = list()
        self.continue_device = list()
        self.client = dict()

    def wifi_device(self):
        data = subprocess.check_output('./device.sh', shell=True)
        self.connect_device = data.decode('utf-8').split('\n')[:-1]

        if sorted(self.connect_device) != sorted(self.continue_device):
            device = list(set(self.connect_device) - set(self.continue_device))
            flag = True

            if not device:
                device = list(set(self.continue_device) - set(self.connect_device))
                flag = False
            
            self.state = False
            self.parse(device, flag)

    def parse(self, device, flag):
        for dev in device:
            data = dev.split()

            if data[3] == 'VICTIM':
                self.state = True

            if flag is True:
                ip = data[0]
                mac = data[1]
                host = data[2]
                status = data[3]
                connect_time = time.strftime('%Y-%m-%d %H:%M:%S')
                start_time = time.time()

                self.client[ip] = [mac, host, status, connect_time, start_time]
            else:
                ip = data[0]
                del self.client[ip]

        self.continue_device = self.connect_device

    def reset(self):
        os.system('clear')

    def frame(self):
        print('-'*162)
        print('|{:^25}|{:^25}|{:^25}|{:^25}|{:^25}|{:^30}|'.format('IP Address', 'MAC Address', 'Device Name', 'Status', 'Connection Time', 'Continuous Time (second)'))
        print('-'*162)

    def show(self):
        for key, value in self.client.items():
            continuous_time = int(time.time() - value[4])
            if self.state is True:
                if value[2] == 'VICTIM':
                    self.victim = value[0]
                    print('|{:^25}|\033[41m{:^25}\033[0m|{:^25}|\033[41m{:^25}\033[0m|{:^25}|{:^30}|'.format(key, value[0], value[1], value[2], value[3], continuous_time))
                elif value[0] == self.victim and (value[2] == 'HOST' or value[2] == 'VM'):
                    print('|{:^25}|\033[44m{:^25}\033[0m|{:^25}|\033[44m{:^25}\033[0m|{:^25}|{:^30}|'.format(key, value[0], value[1], value[2], value[3], continuous_time))
                else:
                    print('|{:^25}|{:^25}|{:^25}|{:^25}|{:^25}|{:^30}|'.format(key, value[0], value[1], value[2], value[3], continuous_time))
            else:
                print('|{:^25}|{:^25}|{:^25}|{:^25}|{:^25}|{:^30}|'.format(key, value[0], value[1], value[2], value[3], continuous_time))
        print('-'*162 + '\n')

    def screen(self):
        self.wifi_device()
        self.reset()
        self.frame()
        self.show()

    def monitor(self):
        while True:
            self.screen()

            print('Number of connected devices : {}'.format(len(self.client)))
