[![N](https://cryptostorm.is/images/bloop.png)](https://cryptostorm.is/)

These configuration files are focused more on compatibility than security.  
They work with OpenVPN => 2.3.2 and OpenSSL => 1.0.0  
The level of security you get with these configs depends on the version of OpenVPN/OpenSSL you have.  
The newer the version, the better the security.  
But even at the least possible security level, the cryptography used is still considered "unbreakable for the foreseeable future".  

If necessary, you can change the port in these configs to anything from 1 to 29999,  
excluding ports 5061 and 5062. Those two are reserved for the [Ed25519](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/ecc/ed25519) and [Ed448](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/ecc/ed448) configs,
and ports 30000-65535 are reserved for [port forwarding](https://cryptostorm.is/portfwd).

See [https://cryptostorm.is/new](https://cryptostorm.is/new) for more information, or just read the comments in these configs.
