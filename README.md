# mca204-networks
Standard Networking Protocols using [flask socketIO](https://github.com/miguelgrinberg/Flask-SocketIO/tree/master/example)


## TODO - Stop and Wait

- need to make Packet # and ACK # separate
- show message : resending >>>> in sender logs 
- prettify everything with bootstrap
- give option between custom message & Packet number on button
- [X] refactor done
- [X] medium now part of handshake
- make packets and acknowledgement
- automate packets as P1, P2, etc. & ack as A1, A2, etc.
- Middle layer needs to work out - drop ack & message
- start a clock each time a packet is sent
- resend the packet if clock is over and acknowledgement is not received
- put proper long comments
- to be told about crashing in the medium logs

## Major

- status in table format - scrollable
- threaded timer
- packet and Ack numbers
- a lot of events and a lot of time

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


## How to run

- git clone the repo
- navigate to directory
- make sure you have pipenv installed, or run `brew install pipenv`
- type `pipenv shell` to activate the virtual environment
- install requirements from requirements.txt or pip lock file
- run `python app.py` and navigate to `localhost:5000` in browser
- disable debugging in app.py if you don't want messages in terminal