#!/usr/bin/python
""" Demonstrate the bitcoind JSON-RPC interface """

import sys
import socket

try:
    from jsonrpc import ServiceProxy
except ImportError:
    print """The demo expects the bitcoin-targeted version of thejsonrpc
package, from https://github.com/jgarzik/python-bitcoinrpc"""
    sys.exit(0)

RPCUSER = "me"        # rpcuser and pw are defined in ~/.bitcoind/bitcoin.conf
RPCPW = "mypassword"  # see https://en.bitcoin.it/wiki/Running_Bitcoin
BTIP = "127.0.0.1"   # by default, bitcoind only accepts localhost connections
BTPORT = "8332"      # the default bitcoind port
BTURL = "http://%s:%s@%s:%s" % ( RPCUSER, RPCPW, BTIP, BTPORT )

PROXY = ServiceProxy(BTURL)

try:
    BTINFO  = PROXY.getinfo()
except socket.error:
    print """Error connecting.
Make sure bitcoind is running on port %s, and is accessible""" % BTPORT
    sys.exit(0)
except ValueError:
    print """Do the rpcuser and rpcpassword parameters match bitcoind.conf?"""
    sys.exit(0)

print "BitCoin stats"

for key in BTINFO.keys():
    print "    %s; %s" % ( key, BTINFO[key] )

print "See https://en.bitcoin.it/wiki/Original_Bitcoin_client/API_Calls_list"
print "for the full list of functions available"
