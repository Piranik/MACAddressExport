#!/bin/bash

str=$(arp -a) 

str=$(echo ${str} | grep en0 | grep -o -E '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}')
python compareMACSerial.py ${str[@]}