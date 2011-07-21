""" BitCoin helper class for PayMe """

from jsonrpc import ServiceProxy

class Bt( object ):
    """ BitCoin JSON-RPC interface class for payme """

    def __init__( self, ip_addr="127.0.0.1", port="8332", user="me",
            password="mypassword",
            app="payme" ):

        bturl = "http://%s:%s@%s:%s" % ( user, password, ip_addr, port )

        self.proxy = ServiceProxy(bturl)
        self.app = app

    def getaddress( self, user ):
        """ Return a unique, persistent BT address for this user.
            Create a new address, if necessary """

        # addresses are tagged in the bitcoin wallet via this naming convention
        account = self.app + "-" + user

        address_list = self.proxy.getaddressesbyaccount( account )

        if( len( address_list ) > 0 ):
            return( address_list[0] )
        
        return self.proxy.getnewaddress( account )


    def getreceived( self, address ):
        """ Return the amount received by this address """

        return "%f" % self.proxy.getreceivedbyaddress( address, 0 )

    def get_user_list( self ):
        """ Return a list of dictionaries containing user ('user'), 
            total received ('amount'), and current balance ('balance') """

        user_list = self.proxy.listreceivedbyaccount( 0, True )

        # limit the list to those fitting the naming convention
        user_list = [ x for x in user_list if x['account'].find(self.app) == 0 ]

        # massage the list to format, add user name, and add balance
        spliceamt = len( self.app ) + 1
        for entry in user_list:
            entry['user'] = entry['account'][spliceamt:]
            entry['amountstr'] = "%f" % entry['amount']
            entry['balance'] = self.proxy.getbalance( entry['account'] )
            entry['balancestr'] = "%f" % entry['balance']

        return( user_list )

    def harvest( self, address ):
        """ transfer all non-zero user balances to 'address' """

        user_list = self.get_user_list()

        [ self.proxy.sendfrom( x['account'], address, x['balance'] ) 
            for x in user_list if x['balance'] > 0 ]

