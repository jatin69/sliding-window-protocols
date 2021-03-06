# mca204-networks

[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

Standard Networking Protocols using [flask socketIO](https://github.com/miguelgrinberg/Flask-SocketIO/tree/master/example)

## new advancements

* sliding window works for gobackN and selective repeat.
* output as expected for base test cases. logs attached.
* might need more time for complex manual test cases. - later
* all good. quick UI revamp and ready.

## quick todo

* [x] shift google font to online version to remove mixed content error
* [x] unipage deployment to heroku

  * merge all three with namespaces and serve in `app.py`
  * test local, test heroku local and deploy

* [x] heroku deployment - aim
* good UX / UI to see the logs
  * [x] font done
  * But design needs rework.

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
  * [x] tested for continuous bursts. All good and async.
* [ ] add capability to timer so it can uniquely identify at state of packet when it is blasted off. Do retain the packet numbers.

## selective repeat

* ~~this current approach won't work~~ approach now updated
* the session handling is too weak right now - still weak
* [x] need to implement sliding window in REAL - done
* ~~that might lead to the update of stop and wait, but that's another case~~ - nope
* [failure log](./example_logs/failed-selective-repeat-1.txt)
* still weak, but handles cases well. [success log](./example_logs/success-selective-repeat.txt)

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

## Project structure

* **Protocols backend**
  * app.py
  * stop-and-wait.py
  * go-back-N.py
* **Protocols frontend**
  * templates/index.html
  * templates/stop-and-wait.html
  * templates/go-back-N.html
* **Static assets**
  * static/bootstrap-4.0.0-dist
  * jquery
  * socket.io

---

* **experimental**
* prettified part of protocols frontend js
  * templates/prettified-stop-and-wait-js
* frontend
  * bootstrap vs skeleton
  * templates/skeleton.html
* **gitignored**
  * skeleton lib
  * heroku dev files
  * node modules
  * package-lock.json
  * official references/

## Deployment

* **In dev mode** (Active currently)

  * Each protocol has different python file, namely `stop-and-wait.py`, `go-back-N.py`
  * These files serve respective html files as well
  * To run a protocol, it's py file needs to be run and the access point for each is `localhost:5000/`

* **In Deployment Mode**
  * All python files for protocols can be merged with each having a different namespace.
  * Now a single `app.py` is sufficient.
  * Similarly, modify html files to serve for different namespaces.
  * Protocols will be then served at `localhost:5000/stop-and-wait`, `localhost:5000/go-back-N`
  * Every protocol running on same socket but with different namespace.
  * dope.

## Future scope

* colors for ack, message, and crashes
* put socketIO functions in separate file if possible
* try sliding - works well - amazing
* status in table format - scrollable
