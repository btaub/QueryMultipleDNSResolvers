# QueryMultipleDNSResolvers
A script to check record status against N public dns resolvers

This tool can be useful if you make frequent DNS changes and need to check propagation status. The full list of resolvers was grabbed from: https://www.lifewire.com/free-and-public-dns-servers-2626062

Required - dnspython http://www.dnspython.org (pip install dnspython or apt install python-dnspython)

## Sample output:

```
% ./QueryMultipleDNSResolvers.py -l public-dns-servers.short akamai.com
[+] Record: 23.211.232.45
[+] Record: 23.47.60.102
[+] Record: 23.47.60.102
[+] Record: 104.117.205.209
[+] Record: 104.117.205.209
[+] Record: 184.27.218.81

4 Unique records for akamai.com:

 104.117.205.209
 184.27.218.81
 23.211.232.45
 23.47.60.102

% ./QueryMultipleDNSResolvers.py -l public-dns-servers.short akamai.com -v

Number of resolvers to be used: 6

[!] RESOLVER: 4.2.2.3
[!] Attempt 1 of 6:
[+] Record: 23.47.60.102
[!] RESOLVER: 209.244.0.3
[!] Attempt 2 of 6:
[+] Record: 23.47.60.102
[!] RESOLVER: 209.244.0.4
[!] Attempt 3 of 6:
[+] Record: 23.47.60.102
[!] RESOLVER: 64.6.64.6
[!] Attempt 4 of 6:
[+] Record: 173.223.13.73
[!] RESOLVER: 64.6.65.6
[!] Attempt 5 of 6:
[+] Record: 23.54.178.31
[!] RESOLVER: 9.9.9.9
[!] Attempt 6 of 6:
[+] Record: 184.27.218.81

4 Unique records for akamai.com:

 173.223.13.73
 184.27.218.81
 23.47.60.102
 23.54.178.31
```
