#!/usr/bin/env python
from threading import Lock
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, disconnect
import time
import random

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()


# def background_thread():
#     """Example of how to send server generated events to clients."""
#     count = 0
#     while True:
#         socketio.sleep(10)
#         count += 1
#         socketio.emit('my_response',
#                       {'data': 'Server generated event', 'count': count})


# @socketio.on('my_event')
# def test_message(message):
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     emit('my_response',
#          {'data': message['data'], 'count': session['receive_count']})


@socketio.on('sendPacketToSenderBackend')
def handling_packet_at_sender_backend(message):
    session['currentPacket'] = session.get('currentPacket', 0) + 1
    emit('sendPacketToSenderFrontend',  {
        'data': message['data'],
        'currentPacket': session['currentPacket']
    })


# Caught by middle layer for manipulation
@socketio.on('SendPacketToMiddleLayerBackend')
def packet_at_middle_layer(message):
    """
    Event : Message caught from server frontend 
    Task  : Manipulate data and send to middle layer frontend
    """
    time.sleep(.1)
    emit('SendPacketToMiddleLayerFrontend', {'data': message['data']})
    time.sleep(.1)


@socketio.on('packetTimerBlast')
def handling_timer_Blast(message):
    # careful here
    if session['currentPacket'] >= message['currentPacket']+1:
        print("No issues. Packet number",
              message['currentPacket'], "successful.")
    else:
        # retransmit
        emit('sendPacketToSenderFrontend', {
             'data': message['data'], 'currentPacket': message['currentPacket']})


# Message to be sent to Receiver
@socketio.on('sendPacketToReceiverBackend')
def packet_at_receiver_backend(message):
    """
    Event : Message received from server middle layer 
    Task  : Forward the message to receiver end
    """
    # increment packet received number here
    session['currentPacket'] = session.get('currentPacket', 0) + 1
    emit('sendPacketToReceiverFrontend', {'data': message['data']})


@socketio.on('sendAckToSenderBackend')
def ack_at_sender_backend(message):
    emit('sendAckToSenderFrontend', {'data': message['data']})


@socketio.on('PackedCrashedAtMiddleLayer')
def handling_packet_crash():
    emit('packedNotReceivedByReceiver')


@socketio.on('sendAckToMiddleLayerBackend')
def ack_at_middle_layer_backend(message):
    # will increase each time a packet is sent
    # current packet number starts with 1
    time.sleep(.1)
    emit('sendAckToMiddleLayerFrontend', {'data': message['data']})
    time.sleep(.1)


# continous pings
@socketio.on('HeyPing')
def ping_pong():
    """
    Event : ping 
    Task  : pong
    """
    emit('HeyPong')


# Server index.html
@app.route('/')
def index():
    """
    Event : User navigates to "localhost:5000" in a new tab
    Task  : Server the "templates/index.html" page to user
    """
    return render_template('index.html', async_mode=socketio.async_mode)


# Accepting connection from client
@socketio.on('connect')
def complete_connection():
    """
    Event : Accept the connection from client (predefined)
    Task  : To complete the connection to this client
    """
    session['currentPacket'] = 0
    emit('server_started')
    # emit('complete_connection', {'data': 'Hi Receiver!'})


@socketio.on('connectionRequestToMiddleLayerBackend')
def connection_request_to_middle_layer(message):
    emit('connectionRequestToMiddleLayerFrontend', {'data': message['data']})


@socketio.on('connectionRequestToSenderBackend')
def connectionRequestToSenderBackend(message):
    if message['data'] == 'Hi Sender!':
        emit('connectionRequestToSenderFrontend', {
             'data': 'Connection established. Hello Receiver!'})
    else:
        emit('connection_failure', {'data': 'Connection denied, Retry!'})


# Requesting termination of connection
@socketio.on('disconnect_request')
def disconnect_request(message):
    """
    Event : User requested connection termination
    Task  : Tie the loose ends, the call the disconnect() event
    """
    emit('disconnecting_confirmation', {
         'data': message['data'] + 'Disconnected!'})


# Server disconnected
@socketio.on('disconnect')
def test_disconnect():
    """
    Event  : Disconnect the server from client (predefined)
    Task   : Receiver Disconnected
    """
    print('Receiver disconnected', request.sid)


# Start the app : dev mode
if __name__ == '__main__':
    """
    Event : Start the server
    Task  : Keep the server running, debugging ON in dev mode
    """
    socketio.run(app, debug=True)
