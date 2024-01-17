[![N](https://cryptostorm.is/images/bloop.png)](https://cryptostorm.is/)

The most recent OpenVPN configuration files for cryptostorm are available here and [here](https://cryptostorm.is/configs/).

The configs in the [rsa](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/rsa) folder are more for compatibility than security. Works with OpenVPN => 2.3.2 and OpenSSL => 1.0.0  
The configs in the [ecc](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/ecc/) folder are more for security than compatibility. Works with OpenVPN => 2.4.0 and OpenSSL => 1.0.1d  
The configs in [ecc/ed25519](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/ecc/ed25519/) and [ecc/ed448](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/ecc/ed448/) work with OpenVPN => 2.4.3 and OpenSSL => 1.1.1  

The level of security you get with these configs depends on the version of OpenVPN/OpenSSL you have.  
The newer the version, the better the security.  
But even at the least possible security level, the cryptography used is still considered "unbreakable for the foreseeable future".

See [https://cryptostorm.is/new](https://cryptostorm.is/new) for more information, or just read the comments in these configs.
