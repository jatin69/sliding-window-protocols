# mca204-networks
Standard Networking Protocols using [flask socketIO](https://github.com/miguelgrinberg/Flask-SocketIO/tree/master/example)


## todo urgent
- refactor done
- proper long comments
- include medium in handshake

## TODO - Stop and Wait

- make packets and acknowledgement
- automate packets as P1, P2, etc. & ack as A1, A2, etc.
- Middle layer needs to work out - drop ack & message
- start a clock each time a packet is sent
- resend the packet if clock is over and acknowledgement is not received

## Major

- threaded timer
- packet and Ack numbers
- a lot of events and a lot of time
- status in table format - scrollable

## Transmission Flow

0. Hi sender & Hi receiver - both connected
1. Packet forms at senderFrontend

2. SendPacketToMiddleLayerBackend
3. SendPacketToMiddleLayerFrontend

4. SendPacketToReceiverBackend
5. sendPacketToReceiverFrontend

6. sendAckToMiddleLayerBackend
7. sendAckToMiddleLayerFrontend

8. sendAckToSenderBackend
9. sendAckToSenderFrontend