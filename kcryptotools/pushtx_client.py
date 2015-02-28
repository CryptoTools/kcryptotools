import sys
import json
import pushtx_server
import pushtx_server_config

def pushtx(tx):

    recvmsg=pushtx_server.communicate(pushtx_server_config.SERVER_IP,pushtx_server_config.SERVER_PORT,tx,pushtx_server_config.BUFFER_SIZE)
    #out = json.loads(recvmsg)

def main():
    if len(sys.argv) < 2: 
        raise Exception('invalid arguments')
    pushtx(sys.argv[1])
   

if __name__ == "__main__":
    main()
