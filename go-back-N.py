#!/usr/bin/env python
from threading import Lock
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, disconnect
import time
import random

# Set this variable to "threading", "eventlet" or "gevent" 
# I used gevent
async_mode = None

# #############################  ### Initialise flask ######################################
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

# ################################# Establish Connection  #####################################

# Accepting connection from client
@socketio.on('connect')
def server_coming_alive():
    """
    From : Predefined event connect. Called when server comes alive.
    Task : Initialise session variables
    To   : Server start message at frontend
    """
    session['currentPacket'] = 0
    session['currentAck'] = 0
    session['expectedAck'] = 0
    emit('server_started')
    # emit('complete_connection', {'data': 'Hi Receiver!'})


@socketio.on('connectionRequestToMiddleLayerBackend')
def connection_request_to_middle_layer_backend(message):
    """
    From : Receiver frontend after receiver said hi to sender
    Task : Simply pass data from receiver front end to middle layer frontend
    To   : Middle layer frontend - to display log
    """
    emit('connectionRequestToMiddleLayerFrontend', {'data': message['data']})


@socketio.on('connectionRequestToSenderBackend')
def connection_request_to_sender_backend(message):
    """
    From : Middle layer frontend
    Task : If receiver greets, then all good. Else, fail connection
    To   : Sender frontend - to display log
    """
    if message['data'] == 'Hi Sender!':
        emit('connectionRequestToSenderFrontend', {
             'data': 'Connection established. Hello Receiver!'})
    else:
        emit('connection_failure', {'data': 'Connection denied, Retry!'})


# ###################################### Ping Pong #######################################

@socketio.on('HeyPing')
def ping_pong():
    """
    From : ping
    Task : simply emit pong and help in roundtrip latency calculation 
    To   : pong
    """
    emit('HeyPong')

# ###################################### Transmission #######################################


@socketio.on('sendPacketToSenderBackend')
def handling_packet_at_sender_backend(message):
    """
    From : Sender Input form OR retransmissions
    Task : initialise session variables
    To   : send Packet to sender frontend
    """
    session['currentPacket'] = session.get('currentPacket', 0) + 1
    session['expectedAck'] = session['currentPacket']
    emit('sendPacketToSenderFrontend',  {
        'data': message['data'],
        'currentPacket': session['currentPacket']
    })


@socketio.on('packetTimerBlast')
def handling_timer_Blast_from_sender(message):
    """
    From : Sender Timer
    Task : If the acknowledgement of previous packet is successfully received. All good.
           else, re transmit the message 
    To   : Middle layer frontend
    """
    print("Timer Blasted for Packet #", message['currentPacket'])
    """
    Case : Missing Packet case
    Explanation : If current packet ( whose timer blasts after 2 seconds ) 
    is still greater (even after 2 seconds ) than 
    packets received by receiver (who should have received atleast 2 more in 2 seconds)
    then something is wrong. Retransmit.

    Case : Missing acknowledgement case
    Explanation : Ack is incremented from receiver side, but is never reached at sender.
    so we decrement the session currentAck whenver ack crashes at middle layer
    that way, currentExpectedAck (equal to currentPack for stop and wait) 
    is always > currentAck

    """
    if message['currentPacket'] > session['currentAck']:
        print("Resending Packet number", message['currentPacket'])
        emit('sendPacketToSenderFrontend', {
             'data': message['data'], 'currentPacket': message['currentPacket']})
    else:
        print("No issues. Packet number", message['currentPacket'], "successful.")


@socketio.on('SendPacketToMiddleLayerBackend')
def handling_packet_at_middle_layer_backend(message):
    """
    From : sender frontend
    Task : provide some visual delay
    To   : Middle layer frontend
    """
    time.sleep(.1)
    emit('SendPacketToMiddleLayerFrontend', {
         'data': message['data'], 'currentPacket': message['currentPacket']})
    time.sleep(.1)


@socketio.on('PackedCrashedAtMiddleLayer')
def handling_packet_crash_at_middle_layer():
    """
    From : Middle Layer frontend
    Task : handle packet crash and display debug log at frontend
    To   : Receiver frontend for debug log
    """
    emit('packedNotReceivedByReceiver')


@socketio.on('sendPacketToReceiverBackend')
def handling_packet_at_receiver_backend(message):
    """
    From : Middle layer frontend
    Task : packet successfully received. Increment the ackNumber to be sent.
    To   : Receiver frontend
    """
    session['currentAck'] = session.get('currentAck', 0) + 1
    emit('sendPacketToReceiverFrontend',
         {'data': message['data'], 'currentPacket': message['currentPacket'], 'currentAck': session['currentAck']})


@socketio.on('sendAckToMiddleLayerBackend')
def handling_ack_at_middle_layer_backend(message):
    """
    From : Receiver frontend
    Task : packet successfully received. Increment the ackNumber to be sent
    To   : Middle layer frontend
    """
    time.sleep(.1)
    emit('sendAckToMiddleLayerFrontend', {
         'data': message['data'], 'currentAck': message['currentAck']})
    time.sleep(.1)


@socketio.on('AckCrashedAtMiddleLayer')
def handling_ack_crash_at_middle_layer(message):
    """
    From : Middle Layer frontend
    Task : handle Ack crash and display debug log at frontend
    To   : Sender frontend for debug log
    """
    print("Ack #", message['currentAck'], "crashed.")
    session['currentAck'] = session['currentAck']-1
    emit('ackNotReceivedBySender')

@socketio.on('sendAckToSenderBackend')
def handling_ack_at_sender_backend(message):
    """
    From : Middle Layer frontend
    Task : Pass on the message and ackNumber
    To   : Sender frontend
    """
    emit('sendAckToSenderFrontend', {
         'data': message['data'], 'currentAck': message['currentAck']})


# ################################# Disconnection events #################################

# Requesting termination of connection
@socketio.on('disconnect_request')
def handling_disconnect_request_at_backend(message):
    """
    From : User requested connection termination
    Task : Tie the loose ends, the call the disconnect() event
    To   : disconnection frontend
    """
    emit('disconnecting_confirmation', {
         'data': message['data'] + 'Disconnected!'})


# Server disconnected
@socketio.on('disconnect')
def test_disconnect():
    """
    From : predefined disconnect event
    Task : Disconnect the server from client
    To   : None. Print logs to console.
    """
    print('Receiver disconnected', request.sid)


# ############################ Serving go back N #####################################

# Server go-back-N.html
# when namespaces are ready - change it to @app.route('/go-back-N')
@app.route('/')
def index():
    """
    From : User navigates to "localhost:5000" in a new tab
    Task : Serve the "templates/index.html" page to user
    To   : None. Wait for events to start.
    """
    return render_template('go-back-N.html', async_mode=socketio.async_mode)


# ################################# Main function #####################################

# Start the app : dev mode
if __name__ == '__main__':
    """
    Event : Start the server
    Task  : Keep the server running, debugging ON in dev mode
    """
    socketio.run(app, debug=True)

# ###################################################################################

# def background_thread():
#     """Example of how to send server generated events to clients."""
#     count = 0
#     while True:
#         socketio.sleep(10)
#         count += 1
#         socketio.emit('my_response',
#                       {'data': 'Server generated event', 'count': count})

# ###################################################################################
