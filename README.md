# QueryMultipleDNSResolvers
A script to check record status against N public dns resolvers

This tool can be useful if you make frequent DNS changes and need to check propagation status. The full list of resolvers was grabbed from: https://www.lifewire.com/free-and-public-dns-servers-2626062

Future improvements will be colorized output and (possibly) output analysis - report differences on record(s).

Required - dnspython http://www.dnspython.org (pip install dnspython or apt install python-dnspython)

## Sample output:

```
$ ./QueryMultipleDNSResolvers.py -l public-dns-servers.short akamai.com
 [+] Record: 23.207.40.217
 [+] Record: 23.207.40.217
 [+] Record: 104.125.60.47
 [+] Record: 23.60.11.13
 [+] Record: 23.54.250.94
 [+] Record: 23.60.11.13

Unique record(s) for akamai.com:

23.207.40.217
23.60.11.13
23.54.250.94
104.125.60.47

$ ./QueryMultipleDNSResolvers.py -l public-dns-servers.short akamai.com -v

Number of resolvers to be used: 6

RESOLVER: 4.2.2.3
 [+] Record: 95.100.58.193
RESOLVER: 209.244.0.3
 [+] Record: 95.100.58.193
RESOLVER: 209.244.0.4
 [+] Record: 104.118.87.213
RESOLVER: 64.6.64.6
 [+] Record: 23.36.217.204
RESOLVER: 64.6.65.6
 [+] Record: 23.56.119.23
RESOLVER: 9.9.9.9
 [+] Record: 104.109.67.178

Unique record(s) for akamai.com:

95.100.58.193
23.56.119.23
104.118.87.213
104.109.67.178
23.36.217.204
```
