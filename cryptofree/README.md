[![N](https://cryptostorm.is/bloop.png)](https://cryptostorm.is/)

These are the configs for our free service, [cryptofree](https://cryptostorm.is/cryptofree).  
The service is capped at about 160kbps down, 130 kbps up.  
It has the same security features as the paid servers, without anything additional such as port forwarding or transparent .onion/.i2p access.  
When using these configs in OpenVPN, any username/password combination will work.  
See [https://cryptostorm.is/new](https://cryptostorm.is/new) for more information, or just read the comments in these configs.  
The level of security you get with these configs depends on the version of OpenVPN/OpenSSL you have.  
The newer the version, the better the security.  
But even at the least possible security level, the cryptography used is still considered "unbreakable for the foreseeable future".

---
These two ECC configuration files are focused more on security than compatibility.  
They work with OpenVPN => 2.4.0, and OpenSSL => 1.0.1d  
If necessary, you can change the port in these configs to anything from 1 to 65534 (excluding 5061 and 5062).  
[cryptofree_secp521r1-udp.ovpn](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/cryptofree/cryptofree_secp521r1-udp.ovpn)  
[cryptofree_secp521r1-tcp.ovpn](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/cryptofree/cryptofree_secp521r1-tcp.ovpn)

---
These four Ed25519/Ed448 configuration files are the same as the two above, except they use non-NIST curves for part of the TLS process.  
They work with OpenVPN => 2.4.3 and OpenSSL => 1.1.1  
The Ed25519 ones only work on port 5061, and the Ed448 ones only work on port 5062.  
[cryptofree_ed448-udp.ovpn](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/cryptofree/cryptofree_ed448-udp.ovpn)  
[cryptofree_ed448-tcp.ovpn](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/cryptofree/cryptofree_ed448-tcp.ovpn)  
[cryptofree_ed25519-udp.ovpn](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/cryptofree/cryptofree_ed25519-udp.ovpn)  
[cryptofree_ed25519-tcp.ovpn](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/cryptofree/cryptofree_ed25519-tcp.ovpn)

---
These two RSA configuration files are focused more on compatibility than security.  
They work with OpenVPN => 2.3.2 and OpenSSL => 1.0.0  
If necessary, you can change the port in these configs to anything from 1 to 65534 (excluding 5061 and 5062)  
[cryptofree_rsa-udp.ovpn](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/cryptofree/cryptofree_rsa-udp.ovpn)  
[cryptofree_rsa-tcp.ovpn](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/cryptofree/cryptofree_rsa-tcp.ovpn)
