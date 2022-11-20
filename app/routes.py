from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from database.models import *

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/api')
def api():
    return render_template("api.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/api/updateweatherinformation', methods=['GET'])
def api_get_current_weatherinformations():
    print("🥰 calls route .../api/get/currentweatherinformation")
    insert_weatherinformation()
    return jsonify("Most current weather informations")

# @app.route('/api/get/currentweatherinformation', methods=['GET'])
# def api_get_current_weatherinformations():
#     print("🥰 calls route .../api/get/currentweatherinformation")
#     weather, wind, sun = modulWeatherInfo()
#     suninfo = {
#      'azimuth': sun.getAzimuth(),
#      'elevation': sun.getElevation(),
#      'sunrise': sun.getTimeSunrise(),
#      'sunset' : sun.getTimeSunset()
#      }
#     inserted_sunposition = insert_sunposition(suninfo)
#     return jsonify(inserted_sunposition)

# @app.route('/api/getallsunpositions', methods=['GET'])
# def api_get_all_sunpositions():
#     print("🥰 calls route .../api/getallsunpositions")
#     return jsonify(get_sunpositions())

# @app.route('/api/getcurrentsunposition', methods=['GET'])
# def api_get_current_sunposition():
#     print("🥰 calls route .../api/getcurrentsunposition")
#     weather, wind, sun = modulWeatherInfo()
#     suninfo = {
#      'azimuth': sun.getAzimuth(),
#      'elevation': sun.getElevation(),
#      'sunrise': sun.getTimeSunrise(),
#      'sunset' : sun.getTimeSunset()
#      }
#     inserted_sunposition = insert_sunposition(suninfo)
#     return jsonify(inserted_sunposition)

# #orignal#
# @app.route('/api/sunpositions', methods=['GET'])
# def api_get_sunpositions():
#     return jsonify(get_sunpositions())

# @app.route('/api/sunposition/<sid>', methods=['GET'])
# def api_get_sunposition(sid):
#     return jsonify(get_sunposition_by_sid(sid))

# @app.route('/api/sunposition/add',  methods = ['POST'])
# def api_add_sunposition():
#     sunposition = request.get_json()
#     return jsonify(insert_sunposition(sunposition))

# @app.route('/api/sunposition/update',  methods = ['PUT'])
# def api_update_sunposition():
#     sunposition = request.get_json()
#     return jsonify(update_sunposition(sunposition))

# @app.route('/api/sunposition/delete/<sid>',  methods = ['DELETE'])
# def api_delete_sunposition(sid):
#     return jsonify(delete_sunposition(sid))

