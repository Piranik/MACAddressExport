#!/bin/bash

MACADDRESSES= arp -a | grep en1 | grep -o -E '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}'
echo $MACADDRESSES
