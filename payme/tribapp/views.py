""" PayMe views """

from django.shortcuts import render_to_response
import bt


def home( request ):
    """ Render the default index page.
        See the 'templates' directory for the html rendered. """

    return render_to_response( 'home.html')

def userinfo( request ):
    """ Render the user page, including the user name and the user's 
        particular pay-to BT address """

    user = request.GET.get('user', 'null' )

    bt_intrfc = bt.Bt()
    address = bt_intrfc.getaddress( user )
    received = bt_intrfc.getreceived( address )

    return render_to_response( 'userinfo.html', { 'user': user,
        'address': address,
        'received': received } )

def summary( request ):
    """ Show the admin page, with a summary of all user accounts with status,
        plus a command to transfer all outstanding balances to an
        outside address """

    bt_intrfc = bt.Bt()

    harvest_addr = request.GET.get( 'address', None )

    if( harvest_addr ):
        bt_intrfc.harvest( harvest_addr )

    userlist = bt_intrfc.get_user_list()

    return render_to_response( 'summary.html', { 'user_list': userlist } )
