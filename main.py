# from app import *
# from database.models import *
# from flask import Flask
# from flask_cors import CORS
# import socket
from gpio.relais import *
from time import sleep

# def setup_web_server(): 
    # hostname = socket.gethostname()
    # hostIP = socket.gethostbyname(hostname)
    # port = 8080
    # app = Flask(__name__)
    # CORS(app, resources={r"/*": {"origins": "*"}})

    # drop_db_table()
    # create_db_table("schema.sql","processcontrol.sql")
    # try: 
    #     app.run(hostIP, port, debug=True)
    #     print("🫡 Server started")
    # except Error as e:
    #     print (f"Starting Server failed - Error: {e}")

if __name__ == '__main__':
    # GPIO.setmode(GPIO.BCM) 
    cluster_0_0 = Relais(4)
    while True: 
        try: 
            cluster_0_0.turn_on()
            sleep(2)
            cluster_0_0.turn_off()
        except KeyboardInterrupt as e: 
            print({e})