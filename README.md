# mca204-networks
Standard Networking Protocols using [flask socketIO](https://github.com/miguelgrinberg/Flask-SocketIO/tree/master/example)


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

## Approach

Flow of packets follow
1. server frontend
2. middlelayer backend
3. middle layer frontend
4. receiver backend
5. receiver frontend