# This is client for pushtx_server.py  
#
# USAGE:
#
# python pusthx_client.py <tx hex>

import sys
import json
import socket

import peersockets
import pushtx_server
import pushtx_server_config

def _initclient(ip,port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((ip,port))
    return s


def _communicate(ip,port,msg,recv_buffer_size):
    s=_initclient(ip,port)
    peersockets.socketsend(s,msg)
    out=peersockets.socketrecv(s,recv_buffer_size)
    s.close()
    return out

def pushtx(tx):
    send_msg='tx '+tx
    recvmsg=_communicate(pushtx_server_config.SERVER_IP,peersockets.MESSAGING_PORT,send_msg,pushtx_server_config.BUFFER_SIZE)

    if recvmsg=='ack':
        return True
    else:
        print("RECVMSG ",recvmsg)
        return False

def main():
    if len(sys.argv) < 2: 
        raise Exception('invalid arguments')
    out=pushtx(sys.argv[1])
    if out==False:
        print("Pushtx failed.")
    else:
        print("Pushtx succeeded.")

if __name__ == "__main__":
    main()
