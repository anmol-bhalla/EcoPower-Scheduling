from flask import Flask, jsonify
from functions import utilities as utils

app = Flask(__name__)

# Retrieve raw event data from the database
@app.route('/api/data/<event>', methods = ['GET']) #get event
def get_event(event):
    # TO DO: query the database for the event data
    return jsonify({'event': event})

# Remove raw event data from the database
@app.route('/api/data/<event>', methods = ['DELETE']) #delete event
def delete_event(event):
    # TO DO: delete event data
    return jsonify({'event': event})

@app.route('/api/data/<event>', methods = ['POST']) #create event
def create_event():
    # TO DO: create event data
    return jsonify({'event': event})

@app.route('/api/data/<event>', methods = ['PUT']) #update an event
def edit_event():
    # TO DO: edit event data
    return jsonify({'event': event})

# Retrieve raw audit data from the database
@app.route('/api/data/<event>/audit', methods = ['GET']) #get audit
def get_audit(audit):
    # TO DO: query the database for the audit data
    return jsonify({'audit': audit})

# Remove raw audit data from the database
@app.route('/api/data/<event>/audit', methods = ['DELETE']) #delete audit
def delete_audit(audit):
    # TO DO: delete audit data
    return jsonify({'audit': audit})

@app.route('/api/data/<event>/audit', methods = ['POST']) #create audit
def create_audit():
    # TO DO: create audit data
    return jsonify({'audit': audit})

# Retrieve user information from User Registration microservice
@app.route('/api/users/<username>', methods = ['GET'])
def get_user(username):
    # TO DO: get user information
    return jsonify({'username': username})


# Retrieve list of user devices from User Registration microservice
@app.route('/api/users/<username>/devices/<deviceid>', methods = ['GET'])
def get_user_devices(username, deviceid):
    # TO DO: get list of user devices
    return jsonify({'username': username, 'deviceid': deviceid})
