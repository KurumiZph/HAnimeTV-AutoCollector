#!/bin/sh
cd /path/to/hanime-auto-coins-plus/
wait
/usr/bin/python3 /path/to/hanime-auto-coins-plus/AIO.py >> /path/to/hanime-auto-coins-plus/autorun.log 2>&1
wait
file="autorun.log"
wait
truncate -s 0 "$file"
wait
