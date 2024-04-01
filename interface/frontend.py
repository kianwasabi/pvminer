import socket
from flask import Flask
#from flask_cors import CORS
from flask import request, render_template
#from database.models import *

class Server: 
    def __init__(self):
        self.hostname = socket.gethostname()
        self.hostIP = "0.0.0.0" #socket.gethostbyname(self.hostname)
        self.port = 8080
        self.app = Flask(__name__)
        self.setup_routes(self)
    @staticmethod
    def setup_routes(self):
        @self.app.route('/', methods=["POST","GET"])
        def home():
            if request.method == "POST":
                selected_cluster = request.form["button"]
            else:
                return render_template("home.html",data="test")
    def run(self):
        try: 
            self.app.run()
            #self.app.run(self.hostIP, self.port, debug=True)
            #CORS(self.app, resources={r"/*": {"origins": "*"}})
        except Error as e:
            print (f"{e}")