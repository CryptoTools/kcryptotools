# This is a server implementation of pushtx.py, where the server accepts 
# transactions to broadcast through TCP/IP
#
# USAGE:
# python pushtx_server.py <crypto>
#
import sys
import socket
import struct

import cryptoconfig
import peersockets
import pushtx_server_config
  
def main():
    if len(sys.argv) < 2:
        raise Exception("invalid arguments, requires crypto as argument")

    crypto = sys.argv[1].lower()
    handler=peersockets.PeerSocketsHandler(crypto)
    while 1:
        handler.run()
  
if __name__ == "__main__":
    main()
