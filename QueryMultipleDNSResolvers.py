#!/usr/bin/env python

import dns.resolver
import argparse

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
        if not line.startswith("#"):
            list_of_resolvers.append(line.strip())

if args.VERBOSE:
    print("\nNumber of resolvers to be used: %s\n" % len(list_of_resolvers))

for q in list_of_resolvers:
    resolver = dns.resolver.Resolver(configure=False)
# This is stupid, I have to make each nameserver it's own list?
    qq = []
    qq.append(q)
    resolver.nameservers = qq
    if args.VERBOSE:
        print('\033[0;91m[!] RESOLVER: %s' % q)
    try:
        resolver.timeout = 10 # Not working, why?
        answer = resolver.query(args.DOMAIN, args.TYPE)
        for rr in answer:
            print("\033[1;32m[+] Record: %s" %rr)
            result.append(str(rr))
    except Exception as e:
        print("Error %s, %r" %(q,e))
# Trap Ctrl-c to bypass slow/unresponive DNS server
    except KeyboardInterrupt:
        print("User cancelled, skipping %s" %q)

print("\033[;1m\n%s Unique record(s) for %s:\n" %(len(set(result)),args.DOMAIN))

for u in sorted(set(result)):
    print("\033[;0m %s" %u)
