#!/bin/bash

ping 192.168.88.255 -c 2
str=$(arp -a) 

str=$(echo ${str} | grep -o -E '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}')
python compareMACSerial.py ${str[@]}

