# mca204-networks

[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

Standard Networking Protocols using [flask socketIO](https://github.com/miguelgrinberg/Flask-SocketIO/tree/master/example)

## Status

> > not running as of 2AM 16 april
> > running as of 3pm 16 april (maybe its a temp fix)
> > kind of temporary fix. Will get to know more in sliding window

## General Implementations

* [x] need to make Packet # and ACK # separate
* [x] show message : resending >>>> in sender logs
* [x] prettify everything with bootstrap
* [x] give option between custom message & Packet number on button
* [x] refactor done
* [x] medium now part of handshake
* [x] make packets and acknowledgement
* [x] automate packets as P1, P2, etc. & ack as A1, A2, etc.
* [x] Middle layer needs to work out - drop ack & message
* [x] start a clock each time a packet is sent
* [x] threaded timer
* [x] resend the packet if clock is over and acknowledgement is not received
* [x] put proper long comments
* [x] to be told about crashing in the medium logs
* [x] refactoring
* [x] index.html
  * [x] sorted by events
  * [x] documented
  * [x] formatted
  * [x] prettify from separate pretty.js
* [x] app.py
  * [x] sorted by events
  * [x] documented
  * [x] formatted
* [x] pretty.js
  * [x] prettier formatting is an acquired taste
* [x] decide flow of Packet and Acknowledgement
  * [x] checkpoints
  * [x] put exact packet numbers in all messages
  * [x] Packet at sender backend
  * [x] packet at receiver backend
  * [x] ack at receiver backend == current pack
  * [x] ack at sender backend
  * [x] add packet crashing
  * [x] add acknowledgement crashing
* [ ] add values such that a timer can exactly identify, which event has occurred and which not maybe use string instead of packet number, maybe status string + packet but pure packet is still important to signify the concept

## Additions

* colors for ack, message, and crashes
* put socketIO functions in separate file if possible
* try sliding - works well - amazing
* status in table format - scrollable

## Transmission Flow

0.  Hi sender & Hi receiver - both connected
1.  Packet forms at senderFrontend
1.  SendPacketToMiddleLayerBackend
1.  SendPacketToMiddleLayerFrontend
1.  SendPacketToReceiverBackend
1.  sendPacketToReceiverFrontend
1.  sendAckToMiddleLayerBackend
1.  sendAckToMiddleLayerFrontend
1.  sendAckToSenderBackend
1.  sendAckToSenderFrontend

## How to run

* git clone the repo
* navigate to directory
* make sure you have pipenv installed, or run `brew install pipenv`
* type `pipenv shell` to activate the virtual environment
* install requirements from requirements.txt or pip lock file
* run `python app.py` and navigate to `localhost:5000` in browser
* disable debugging in app.py if you don't want messages in terminal
