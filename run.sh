#!/bin/sh
if [ `whoami` != root ]; then
    echo You need root privileges to run this program
    exit
fi
python program/main.py
