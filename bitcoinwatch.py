#! /usr/bin/env python
""" module to monitor realtime Bitcoin transactions via the freenode
#Bitcoin-Watch channel - https://en.bitcoin.it/wiki/Bitcoin-Watch

requires irclib (repo) 
and ircbot 
  (http://code.google.com/p/ircbot-collection/source/browse/trunk/ircbot.py?r=66)

pygame is used by the demo main routine"""

from ircbot import SingleServerIRCBot
from irclib import nm_to_n
import re
import random

class BitcoinWatchBot(SingleServerIRCBot):
    """ Bitcoin transaction watching bot. See main() for usage example """

    def __init__(self, channel="#Bitcoin-Watch",
                       nickname="bcbot",
                       server="chat.freenode.net",
                       port=6667,
                       realname="Bitcoin monitoring bot https://github.com/davesteele/python-bitcoin-talk"):
        SingleServerIRCBot.__init__(self, [(server, port)], nickname, realname)
        self.channel = channel

        self.txCallbacks = []

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + str( random.randint( 0, 32768 ) ) )

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_pubmsg(self, c, e):

        if( nm_to_n(e.source()) != 'ljrbot' ):
            return

        # remove color setting and underline escapes from the message
        msg = re.sub( "\03[0-9]{1,2},[0-9]{1,2}", "", e.arguments()[0] )
        msg = re.sub( "\037", "", msg )

        txmsg = re.match( "^Txn (.+):(.+)$", msg )
        txval = 0
        addrs = []
        if( txmsg ):
            for addrStr in txmsg.group(2).split(","):
                addrRe = re.search( '([0-9a-zA-Z]+) ([0-9\.]+) BTC', addrStr )
                if addrRe:
                    val = float( addrRe.group(2) )

                    addrs.append( ( addrRe.group(1), val ) )

                    txval = txval + val

            for ( func, xarg ) in self.txCallbacks:
                func( txmsg.group(1), txval, addrs, xarg )

    def add_tx_callback( self, func, extra_arg ):
        """ Add a callback which is called for each transaction entry
        ala func( transaction_id, transaction_value, addrs, xtra_arg )
        addrs is a list of ( <bitcoin_addr>, <val> )"""

        self.txCallbacks.append( ( func, extra_arg ) )
                    
def main():

    import pygame.mixer

    mixer = pygame.mixer
    mixer.init(11025)
    sound = mixer.Sound( "data/cashreg.wav" )

    bot = BitcoinWatchBot( )

    # callback to be called on each transaction record
    def txcb( tx, val, addrs, sound ):
        print "Transaction -", tx, val

        for addr in addrs:
            print "    Address -", addr[0], addr[1]

        sound.play()

    bot.add_tx_callback( txcb, sound )

    bot.start()

if __name__ == "__main__":
    main()
