from flask import Flask
from flask import jsonify, request

""" required interaces from eco-power registration """
def getUser(username):
    user = jsonify({'username': username})
    parent_url = "http://127.0.0.1:5000/api/data/" + registration
    output = request.delete(parent_url)
    print(output)

def getDevices(username):
    devices = jsonify({'username': username})
    parent_url = "http://127.0.0.1:5000/api/data/" + registration


""" provided interfaces, more internal to us """
def getTechnicianSchedule(month, year):
    parent_url = "http://127.0.0.1:5000/api/technicians/"
    output = request.get(parent_url)
    print(output)

def getCalendar(month, year):
    parent_url = "http://127.0.0.1:5000/api/calendar/"
    output = request.get(parent_url)
    print(output)

def getAuditChecklist(user, devices):
    parent_url = "http://127.0.0.1:5000/api/users/" + username
    output = request.get(parent_url)
    print(output)

def rescheduleAppointment(appointment, newAppointment):
    parent_url = "http://127.0.0.1:5000/api/calendar/" + appointment
    output = request.put(parent_url)
    print(output)

def getScheduledAppointment(username):
    parent_url = "http://127.0.0.1:5000/api/users/" + username
    output = request.get(parent_url)
    print(output)

def scheduleAppointment(newAppointment):
    parent_url = "http://127.0.0.1:5000/api/calendar/" + newAppointment
    output = request.post(parent_url)
    print(output)

def saveAuditResults(auditResults):
    parent_url = "http://127.0.0.1:5000/api/results/" + auditResults
    output = request.post(parent_url)
    print(output)

def auditResultsAvail(appointment):
    parent_url = "http://127.0.0.1:5000/api/calendar/" + appointment
    output = request.get(parent_url)
    print(output)


def getAuditResults(appointment):
    parent_url = "http://127.0.0.1:5000/api/calendar/" + appointment
    output = request.get(parent_url)
    print(output)
