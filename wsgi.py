import socket
import os
import time


from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    dir = "/mnt/"
    fn = dir + "log.txt"


    file = open(fn, 'w')
    file.write("Hostname: " + str(socket.gethostname()) + " Timestamp: " + str(time.time()))
    file.close()

    file = open(fn, 'r')
    return file.read()


if __name__ == "__main__":
    application.run()
