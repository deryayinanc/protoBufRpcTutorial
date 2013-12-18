#!/usr/bin/python
import tutorial_pb2 as proto

__author__ = 'derya yinanc'


'''
Client side code is based on a google protobuf sample code developed by authors below
that is packaged as an example with protobuf-rocketrpc package.



Authors: Martin Norbury (mnorbury@lcogt.net)
         Eric Saunders (esaunders@lcogt.net)
         Zach Walker (zwalker@lcogt.net)
         Jan Dittberner (jan@dittberner.info)


'''

import argparse
import socket
from protobuf.socketrpc import RpcService

import logging
log = logging.getLogger(__name__)
hostname = 'localhost'
port = 8090


if __name__ == '__main__':

    #Command line argument handling
    parser = argparse.ArgumentParser(description='This is a demo script by Derya Yinanc.')
    parser.add_argument('-i','--host', help='HostName/IP',required=True)
    parser.add_argument('-p','--port',help='Port', required=True)
    parser.add_argument('-c','--command',help='Command', required=True)
    args = parser.parse_args()

    try:
        # Create request message
        request = proto.CommandRequest()
        if(args.command == "POWER_OFF"):
            command = proto.POWER_OFF
        elif(args.command == "POWER_ON"):
            command = proto.POWER_ON
        else:
            raise NameError('Command Not in Dictionary')
        request.credentials = socket.gethostbyname(socket.gethostname())
        request.command = command
    except Exception, ex:
       print(ex)
    except NameError:
        print('Command supplied does not exist in dictionary %s', args.command)
        raise






    service = RpcService(proto.PoshService_Stub, int(args.port), args.host)

    try:
        request.IsInitialized()
        response = service.getCommandResponse(request, timeout=1000)
        if response is None:
            raise Exception('service not responding')
        print(response)
    except Exception, ex:
        print(ex)
