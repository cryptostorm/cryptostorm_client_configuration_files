These configuration files are for the new ECC instances, which  
provide the best/strongest crypto available to OpenVPN at the moment.  
Further information about the options used can be found as commments  
inside these files.

OpenVPN 2.4.x is required to use these configs.

Unlike the old ones, these new instances will be cross-platform.  
OS dependent options such as --block-outside-dns and --register-dns  
will be sent to the client via --push commands.  
This will cause a non-fatal error if, for example, you connected to   
the ECC instances from Linux/Android/Mac.  
Those errors can be safely ignored.

I.e., from Debian:
```
Options error: Unrecognized option or missing or extra parameter(s) in [PUSH-OPTIONS]:1: register-dns (2.4.0)
Options error: Unrecognized option or missing or extra parameter(s) in [PUSH-OPTIONS]:7: block-outside-dns (2.4.0)
```
But the connection is still successful.

A new version of the Windows widget will be released shortly, which  
will include support for these ECC instances.
