Don't forget to disable IPv6 with the commands:
```
sysctl -w net.ipv6.conf.all.disable_ipv6=1
sysctl -w net.ipv6.conf.default.disable_ipv6=1
sysctl -w net.ipv6.conf.lo.disable_ipv6=1
```

To disable IPv6 permanently, add to /etc/sysctl.conf:
```
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
```

For some Ubuntu versions, you may need to add this to your OpenVPN config in order to prevent DNS leaks:
```
script-security 2
up /etc/openvpn/update-resolv-conf
down /etc/openvpn/update-resolv-conf
```

A rough script is included that will allow you to connect to connect to a server without having to include any vpn commands.
To use the script just run it
```
sudo cryptostorm.py
```

the script includes a killswitch this will block all connections by default other than from the tun0 interface.
```
sudo cryptostorm.py --killswitch
```

If the script exits incorrectly then the killswitch will need to be disabled
```
sudo cryptostorm.py --disable_killswitch
```

The script also allows for an auth file to be used instead of providing username and password manually. All you have to do is create in this directory a file called auth.conf and in the first line add your token and in the second line add any password.

See auth.conf.example.

If you need to pass any extra parameters to openvpn just use
```
sudo cryptostorm.py --extraparams "--script-security 2 --anotheropenvpnparam"
```
