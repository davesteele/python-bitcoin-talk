#!/usr/bin/python


from jsonrpc import ServiceProxy

PROXY = ServiceProxy( "http://me:mypassword@127.0.0.1:8332" )

BTINFO  = PROXY.getinfo()

print "BitCoin stats"

for key in BTINFO.keys():
    print "    %s; %s" % ( key, BTINFO[key] )

print "See https://en.bitcoin.it/wiki/Original_Bitcoin_client/API_Calls_list"
print "for the full list of functions available"
