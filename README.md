protoBufRpcTutorial
===================

Protobuf RPC Tutorial.

Was asked to build a server-client system based on Google's Protocol buffer technology that can communicate through IP.
Protobuf is a great library for serializing data and getting it ready for transport. However it does not have an RPC layer,
Protobuf-rpc library handles that problem while suffering from lack of documentation and lack of tutorials.

Protocol buffer:
https://code.google.com/p/protobuf/

Protocol buffer RPC:
https://code.google.com/p/protobuf-socket-rpc/

This package contains:
1. tutorial.proto -- definitions.
2. client -- client that will be used to send command request to server.
3. server -- receive, interpret and send a response back.

Parameters defined and usable through command prompt.

Server launch must precede client obviously.

Dependencies: protobuf and protobuf-rpc libraries.
