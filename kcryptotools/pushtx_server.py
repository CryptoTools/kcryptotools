# This is a server implementation of pushtx.py, where the server accepts 
# transactions to broadcast through TCP/IP
#
# USAGE:
# python pushtx.py <crypto> <number of peers to send tx to>
#

import sys
import socket
import struct
import cryptoconfig
import peersockets
import SocketServer

import pushtx_server_config

def socketrecv(conn,init_buffer_size):
    msg=conn.recv(init_buffer_size)

    # None will be received when socket is closed
    if len(msg) == 0:
        return None
    expected_msg_len=struct.unpack('<H',msg[0:2])[0] #length of message in bytes,including this message length byte
    if len(msg) < expected_msg_len:
        while 1:
            new_msg=conn.recv(expected_msg_len-len(msg))
            msg+=new_msg
            if len(msg) == expected_msg_len:
                break                                
    return msg[2:]

def socketsend(conn,msg):
    if len(msg) > 65536:
        raise Exception('message length must be less than 16 bits')
    msg_len=len(msg)+2

    send_msg=struct.pack('<H',msg_len)+msg
    conn.sendall(send_msg)

def initclient(ip,port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))
    return s



def communicate(ip,port,msg,recv_buffer_size):
    s=initclient(ip,port)
    socketsend(s,msg)
    out=socketrecv(s,recv_buffer_size)
    s.close()
    return out

class Handler(SocketServer.BaseRequestHandler):

    def __init__(self,request,client_address,server):
        SocketServer.BaseRequestHandler.__init__(self,request,client_address,server) 

    def handle(self):
        crypto='bitcoin'
        handler=peersockets.PeerSocketsHandler(crypto)
        for address in cryptoconfig.DNS_SEEDS[crypto]:
            handler.create_peer_socket(address)

        while 1:
            handler.run()
            msg=socketrecv(self.request,pushtx_server_config.BUFFER_SIZE)
            out_json={}
            if msg==None:
                return 
            else:
                handler.add_new_broadcast_tx(msg) 
 
def main():
    if len(sys.argv) < 2:
        raise Exception("invalid arguments")

    crypto              = sys.argv[1].lower()
    
    server=SocketServer.TCPServer( ("localhost",pushtx_server_config.SERVER_PORT),Handler)
    server.serve_forever()

if __name__ == "__main__":
    main()
