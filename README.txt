kcryptotools - Kay's Crypto Tools by Umpei Kay Kurokawa
v 0.0 

INTRODUCTION:

kcryptotools is a collection of python programs designed to connect to a crypto network, talk to peers, and gather information. It is designed to work with Bitcoin and any closely related forks. Curently it supports Bitcoin, Litecoin, and Dogecoin. 

It is not a full node, as it does not have any knowledge regarding the blockchain. Some of the code in protocol.py is taken from Caesure by Sam Rushing (https://github.com/samrushing/caesure). This software is in alpha and should not be used for production. 

Coded with Python 2.7 and tested with Ubuntu 12.04/14.04. No support for Python 3 yet.  

CURRENT FEATURES:

Connect to Bitcoin/Litecoin/Dogecoin nodes and broadcast transactions 

USAGE:

python pushtx.py <crypto> <number of peers to send tx to> <transaction1 in hex> <transaction2 in hex> ...

This will connect to crypto nodes and broadcast the transactions in hex. Note that there is no check done on the transaction's validity, so this is useful for sending some transactions that would be labeled as invalid by bitcoind or blockchain.info's pushtx (i.e, tx's utilizing OP_RETURN).


KNOWN ISSUES:

Please submit any issues you find at https://github.com/kaykurokawa/kcryptotools/issues

TODO LIST: 

Python 3 support 

