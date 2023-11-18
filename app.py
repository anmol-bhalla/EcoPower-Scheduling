from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os


app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://bqafdzmwdkhjrn:07623061f89a9b916aae8121938773b6e6020aae7688a93c875f301960aeb4bd@ec2-34-202-53-101.compute-1.amazonaws.com:5432/df70jf2v65kau1'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Technician(db.Model):
    __tablename__ = 'technician'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Appointment(db.Model):
    __tablename__ = 'appointment'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    t_id = db.Column(db.Integer, db.ForeignKey('technician.id'), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    confirmation_status = db.Column(db.String(120), nullable=False)

# TECHNICIAN ROUTES
@app.route("/api/technician/<username>", methods=['GET'])
def get_technicians(username):
    technicians = Technician.query.filter_by(username=username).first()
    if technicians:
        return jsonify({
            'id': technicians.id,
            'username': technicians.username,
            'email': technicians.email
        })
    else:
        return jsonify({"Message": "No technicians found!"})
    
@app.route("/api/technician", methods=['POST'])
def create_technicians():
    data = request.json
    technician = Technician(username=data['username'], email=data['email'])
    db.session.add(technician)
    db.session.commit()
    return jsonify({'message': 'Technician registered successfully!'})


# APPOINTMENT ROUTES
@app.route("/api/appointment/<id>", methods=['GET'])
def get_appointments(t_id):
    appointments = Appointment.query.filter_by(t_id=t_id).first()
    if appointments:
        return jsonify({
            'id': appointments.id,
            'user_id': appointments.user_id,
            't_id': appointments.t_id,
            'time': appointments.time,
            'confirmation_status': appointments.confirmation_status
        
        })
    
    else:
        return jsonify({"Message": "No appointments found!"})
    
@app.route("/api/appointment", methods=['POST'])
def create_appointment():
    data = request.json
    appointment = Appointment(user_id=data['user_id'], t_id=data['t_id'], time=data['time'], confirmation_status=data['confirmation_status'])
    db.session.add(appointment)
    db.session.commit()
    return jsonify({'message': 'Appointment created successfully!'})

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
def create_event(event):
    # TO DO: create event data
    return jsonify({'event': event})

@app.route('/api/data/<event>', methods = ['PUT']) #update an event
def edit_event(event):
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
def create_audit(event):
    # TO DO: create audit data
    return jsonify({'event': event})

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

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=9000)