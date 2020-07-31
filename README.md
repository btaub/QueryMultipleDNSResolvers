# QueryMultipleDNSResolvers
A script to check record status against N public dns resolvers

This tool can be useful if you make frequent DNS changes and need to check propagation status. The full list of resolvers was grabbed from: https://www.lifewire.com/free-and-public-dns-servers-2626062

Required - dnspython http://www.dnspython.org (pip install dnspython or apt install python-dnspython)

## Sample output:

```
$ ./QueryMultipleDNSResolvers.py -l public-dns-servers.short akamai.com
[+] Record: 104.121.219.185
[+] Record: 104.108.37.78
[+] Record: 104.121.219.185
[+] Record: 104.108.37.78
[+] Record: 23.0.87.23
[+] Record: 23.55.1.49

4 Unique records for akamai.com:

 104.108.37.78
 104.121.219.185
 23.0.87.23
 23.55.1.49

$ ./QueryMultipleDNSResolvers.py -l public-dns-servers.short akamai.com -v

Number of resolvers to be used: 6

[!] RESOLVER: 4.2.2.3
[+] Record: 104.108.37.78
[!] RESOLVER: 209.244.0.3
[+] Record: 2.19.135.23
[!] RESOLVER: 209.244.0.4
[+] Record: 104.121.219.185
[!] RESOLVER: 64.6.64.6
[+] Record: 104.108.37.78
[!] RESOLVER: 64.6.65.6
[+] Record: 23.0.87.23
[!] RESOLVER: 9.9.9.9
[+] Record: 23.214.44.12

5 Unique records for akamai.com:

 104.108.37.78
 104.121.219.185
 2.19.135.23
 23.0.87.23
 23.214.44.12
```
