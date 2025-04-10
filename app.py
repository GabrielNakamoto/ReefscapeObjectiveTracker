from networktables import NetworkTables
from flask import Flask, request, jsonify
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

real_robot = False
server_ip = '10.41.52.2' if real_robot else '127.0.0.1'

NetworkTables.initialize(server=server_ip)
table = NetworkTables.getTable('SmartDashboard')
# 'Application Programming Interface'
# API: let someone else access your program, one that usually runs on a server,
# through requests ex:
#   send data (POST / PUT), receive data (GET), modify data (DELETE)

# assign function to url
@app.route('/send-objective', methods=['POST'])
def send_objective():
    table.putString('CoralObjective', request.form['objective'])
    return f"Sent {request.form['objective']}!"

@app.route('/')
def render_html():
    return open("reef.html").read()

if __name__ == '__main__':
    app.run(port=5000)
