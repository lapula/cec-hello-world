import socket
import os
import time


from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    dir = "./mnt/"
    fn = dir + "log.txt"

    if os.path.exists(fn):
        append_write = 'a'
    else:
        append_write = 'w'

    file = open(fn, append_write)
    file.write("Hostname: " + str(socket.gethostname()) + " Timestamp: " + str(time.time()) + " <br>")
    file.close()

    file = open(fn, 'r')
    return file.read()


if __name__ == "__main__":
    application.run()
