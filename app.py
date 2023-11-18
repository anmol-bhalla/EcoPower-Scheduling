from flask import Flask, jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#stuff added on nov 1:

#DATABASE_URL = 'postgresql://myappuser:password@localhost/schedulingdb'
DATABASE_URL= 'postgresql://bqafdzmwdkhjrn:07623061f89a9b916aae8121938773b6e6020aae7688a93c875f301960aeb4bd@ec2-34-202-53-101.compute-1.amazonaws.com:5432/df70jf2v65kau1'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)

#add info about possible tables eg: technician, calender

class Technician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(80), unique=True, nullable=False)
    confirmation_status = db.Column(db.Integer, db.ForeignKey('technician.id'), nullable=False)


#Implement the post requests of your APIs

@app.route('/api/technician', methods=['POST'])
def register_technician():
    data = request.json
    new_tech = Technician(username=data['username'], email=data['email'])
    db.session.add(new_tech)
    db.session.commit()
    return jsonify({'message': 'Technician registered successfully!'})

@app.route('/api/appointment', methods=['POST'])
def appointment_setup():
    data = request.json
    new_appointment = Appointment(time=data['time'], confirmation_status=data['confirmation_status'])
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify({'message': 'Appoitment updated successfully!'})

#stuff added for nov 1 ends**

@app.route("/")
def root():
    return jsonify({"Message": "Welcome to the Scheduling API!"})

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


#getting flask to run:

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)