#!/bin/bash
if [ "x$1" == "xENABLE" ]; then
    
    ufw default deny outgoing
    ufw default deny incoming
    ufw allow out on tun0 from any to any

    ufw --force enable

    echo "Kill switch enabled."
else
    ufw --force reset
    ufw --force disable
    echo "Kill switch disabled."
fi

