#!/bin/bash

str=$(arp -a) 

str=$(echo ${str} | grep -o -E '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}')
python compareMACSerial.py ${str[@]}