#!/usr/bin/python
import tutorial_pb2 as proto

__author__ = 'derya yinanc'



'''
Server side code is based on a google protobuf sample code developed by authors below
that is packaged as an example with protobuf-rocketrpc package.


Authors: Martin Norbury (mnorbury@lcogt.net)
         Eric Saunders (esaunders@lcogt.net)
         Zach Walker (zwalker@lcogt.net)
         Jan Dittberner (jan@dittberner.info)

'''

# Add main protobuf module to classpath
import argparse
import sys
sys.path.append('../../main')

from protobuf.socketrpc.server import SocketRpcServer

import logging
import random

log = logging.getLogger(__name__)
port = 8090


class PoshService(proto.PoshService):
    '''An example service implementation.'''

    def getCommandResponse(self, controller, request, done):
        '''Get the current time and return as a response message via the
        callback routine provide.'''
        log.info('Called TestMethod')

        # Create response message
        respRand = random.randint(0,1)
        response = proto.CommandResponse()
        if (respRand == 1):
            response.response = proto.RES_OK
            response.response_message = 'success '
        elif(respRand == 0):
            response.response = proto.RES_ERR
            response.response_message = 'failure '
        try:
            response.response_message += proto._COMMAND.values_by_number[request.command].name
        except Exception,ex:
            response.response = proto.RES_ERR
            response.response_message = 'This command is not acceptable: ' + str(ex)



        # Call provided callback with response message
        done.run(response)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='This is a demo script by Derya Yinanc.')
    parser.add_argument('-p','--port',help='Port', required=True)
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG)

    # Create service
    try:
        service = PoshService()
        server = SocketRpcServer(int(args.port),host='')
        server.registerService(service)
        server.run()
    except Exception, ex:
        print (ex)

