import socket
import os
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    os.listdir("/mnt/")
    return "Hello World! Greetings from "+socket.gethostname()+"\n"


if __name__ == "__main__":
    application.run()
