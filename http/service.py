from flask import Flask
from flask import request
import os
import requests
import socket
import sys

app = Flask(__name__)

@app.route('/service/<service_number>')
def hello(service_number):
    return (
        'This is behind Envoy (service {})! hostname: {} resolved'
        'hostname: {}\n'.format(
            os.environ['SERVICE_NAME'], socket.gethostname(),
            socket.gethostbyname(socket.gethostname())))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
