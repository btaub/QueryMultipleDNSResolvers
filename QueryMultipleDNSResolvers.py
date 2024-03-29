#!/usr/bin/env python3

import dns.resolver
import argparse
import socket

result = []

# Handle arguments
parser = argparse.ArgumentParser(description="A script to check record status against N public dns resolvers",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("DOMAIN",help="The domain you want record(s) for")
parser.add_argument("-t","--TYPE",help="Type of DNS record to query for (A,AAAA,CNAME, etc).",default="A")
parser.add_argument("-l","--LIST_OF_NAMESERVERS",help="List of nameservers to query in a separate text file.",default="public-dns-servers.full")
parser.add_argument("-v","--VERBOSE",action="store_true",help="Verbose output",default=False)
args = parser.parse_args()

# Ingest list of nameservers. Commenting out dead servers is supported
with open(args.LIST_OF_NAMESERVERS) as servers:
    list_of_resolvers = []
    for line in servers:
        if not line.startswith('#') and not line.startswith('\n'):
            list_of_resolvers.append(line.strip())

if args.VERBOSE:
    print("\nNumber of resolvers to be used: %s\n" % len(list_of_resolvers))

for _ns in list_of_resolvers:
    idx_ns = list_of_resolvers.index(_ns)
    idx_ns += 1 # Since we start at 0
    resolver = dns.resolver.Resolver()
    resolver.lifetime = 1

    ns = []
    ns.append(_ns)
    resolver.nameservers = ns
    if args.VERBOSE:
        print('\033[0;91m[!] Attempt %s of %s: ' %(idx_ns,len(list_of_resolvers)))
        print('\033[0;91m[!] RESOLVER: %s' % _ns)
    try:
        answer = resolver.resolve(args.DOMAIN, args.TYPE)
        for rr in answer:
            print("\033[1;32m[+] Record: %s" %rr)
            result.append(str(rr))

    except Exception as e:
        print("Error %s, %r" %(_ns,e))
# Trap Ctrl-c to bypass slow/unresponive DNS server
    except KeyboardInterrupt:
        print("User cancelled, skipping %s" %_ns)

if len(set(result)) == 1:
    print("\033[;1m\n%s Unique record for %s:\n" %(len(set(result)),args.DOMAIN))
else:
    print("\033[;1m\n%s Unique records for %s:\n" %(len(set(result)),args.DOMAIN))

for rec in sorted(set(result)):
    print("\033[;0m %s" %rec)

print('')
