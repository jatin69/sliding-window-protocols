# mca204-networks

[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

Standard Networking Protocols using [flask socketIO](https://github.com/miguelgrinberg/Flask-SocketIO/tree/master/example)

* refactoring

  * [x] index.html
    * [x] sorted by events
    * [x] documented
    * [x] formatted
    * [x] prettify from separate pretty.js
  * [x] app.py
    * [x] sorted by events
    * [x] documented
    * [x] formatted
  * pretty.js
    * prettier formatting is an acquired taste

### MAJOR

> > not running as of 2AM 16 april
> > running as of 3pm 16 april (maybe its a temp fix)

* decide flow of Packet and Acknowledgement
  * checkpoints
  * Packet at sender backend
  * packet at receiver backend
  * ack at receiver backend == current pack
  * ack at sender backend
* add values such that a timer can exactly identify, which event has occurred and which not
* maybe use string instead of packet number, maybe status string + packet
* but pure packet is still important to signify the concept

> > > > > > > kind of temporary fix. Will get to know more in sliding window

* colors for ack, message, and crashes
* put socketIO functions in separate file if possible
* [x] put exact packet numbers in all messages
* try sliding - works well - amazing
* add acknowledgement crashing

  * to handle this, i need to introduce expected ack

* [x] packet crashed - handled
* ack crashed - to be handled

## TODO - Stop and Wait

* need to make Packet # and ACK # separate
* show message : resending >>>> in sender logs
* prettify everything with bootstrap
* give option between custom message & Packet number on button
* [x] refactor done
* [x] medium now part of handshake
* make packets and acknowledgement
* automate packets as P1, P2, etc. & ack as A1, A2, etc.
* Middle layer needs to work out - drop ack & message
* start a clock each time a packet is sent
* resend the packet if clock is over and acknowledgement is not received
* put proper long comments
* to be told about crashing in the medium logs

## Major

* status in table format - scrollable
* threaded timer
* packet and Ack numbers
* a lot of events and a lot of time

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
