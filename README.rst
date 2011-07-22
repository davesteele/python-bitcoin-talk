====================================
Exchange Digital Money using Bitcoin
====================================

The Presentation for this talk is at http://davesteele.github.com/python-bitcoin-talk/

For Linux, you will want to install the following packages to use these demos:
   * git
   * python-simplejson
   * python-irclib
   * pygame
   * Django

Make a local copy of this repository with:

   ``git clone git://github.com/davesteele/python-bitcoin-talk.git``

**Simple JSON-RPC Demo**

+---------------+--------------------+
| bitcoincli.py | bitcoinclishort.py |
+---------------+--------------------+

The demo uses a local snapshot of the bitcoin-targeted jsonrpc_ package.
It requires python-simplejson.

.. _jsonrpc: https://github.com/jgarzik/python-bitcoinrpc

The `Bitcoin JSON-RPC API`_ and the `RPC Calls`_ are documented in the
`Bitcoin Wiki`_.

.. _Bitcoin JSON-RPC API: https://en.bitcoin.it/wiki/API_reference_(JSON-RPC)
.. _RPC Calls: https://en.bitcoin.it/wiki/Original_Bitcoin_client/API_Calls_list
.. _Bitcoin Wiki: https://en.bitcoin.it/wiki/Main_Page

**Web Application**

+-------+
| payme |
+-------+

A simple Django web application which demonstrates working with Bitcoin. The
Bitcoin wallet is used to hold the data model. See the README in the payme
directory for details.

The demo requires Django_.

.. _Django: https://www.djangoproject.com/

**Bitcoin Transaction Monitor**

+-----------------+
| bitcoinwatch.py |
+-----------------+

Defines a module that Watches the BitcoinWatch_ IRC channel and uses registered
callback functions to flag every transaction seen there.

.. _BitcoinWatch: http://webchat.freenode.net/?channels=#Bitcoin-Watch

This demo uses a local snapshot of the ircbot_ library. It requires
python-irclib, and pygame for the demo mode.

.. _ircbot: http://code.google.com/p/ircbot-collection/source/browse/trunk/ircbot.py?r=66
