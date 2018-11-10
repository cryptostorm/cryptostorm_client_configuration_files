[![N](https://cryptostorm.is/bloop.png)](https://cryptostorm.is/)
These are the configs for our free service, [cryptofree](https://cryptostorm.is/cryptofree)
The service is capped at about 160kbps down, 130 kbps up.
It has the same security features as the paid servers, without anything additional such as port forwarding or transparent .onion/.i2p access.
When using these configs in OpenVPN, any username/password combination will work.
See [https://cryptostorm.is/new](https://cryptostorm.is/new) for more technical information on the differences between these configs.
---
[cryptofree_rsa-udp.ovpn](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/cryptofree/cryptofree_rsa-udp.ovpn) is the UDP config that uses an RSA server certificate along with a secp521r1 CA certificate.
[cryptofree_rsa-tcp.ovpn](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/cryptofree/cryptofree_rsa-tcp.ovpn) is the TCP config that uses an RSA server certificate along with a secp521r1 CA certificate.
`Almost any version of OpenVPN/OpenSSL will work with the RSA configs.`
---
[cryptofree_secp521r1-udp.ovpn](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/cryptofree/cryptofree_secp521r1-udp.ovpn) is the UDP config that uses only secp521r1 certificates.
[cryptofree_secp521r1-tcp.ovpn](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/cryptofree/cryptofree_secp521r1-tcp.ovpn) is the TCP config that uses only secp521r1 certificates.
`At least OpenVPN 2.4.x is required for the secp521r1 configs.`
---
[cryptofree_ed448-udp.ovpn](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/cryptofree/cryptofree_ed448-udp.ovpn) is the UDP config that uses only Ed448 certificates.
[cryptofree_ed448-tcp.ovpn](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/cryptofree/cryptofree_ed448-tcp.ovpn) is the TCP config that uses only Ed448 certificates.
[cryptofree_ed25519-udp.ovpn](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/cryptofree/cryptofree_ed25519-udp.ovpn) is the UDP config that uses only Ed25519 certificates.
[cryptofree_ed25519-tcp.ovpn](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/cryptofree/cryptofree_ed25519-tcp.ovpn) is the TCP config that uses only Ed25519 certificates.
`The latest OpenVPN AND OpenSSL 1.1.1 is required for the Ed448 or Ed25519 configs.`

