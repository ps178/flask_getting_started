
from flask import Flask, jsonify, request

from scipy.spatial import distance

app = Flask(__name__)

@app.route('/name', methods=["GET"])
def name():
    Name = {
        "name": "My name is Petek"
    }
    return jsonify(Name)



@app.route("/hello/<name>", methods = ["GET"])
def hello(name):
 
    data = {
        "message": "Hello there, {0}".format(name)
    }

    return jsonify(data)


@app.route("/distance" ,methods = ["POST"])
def ditance():
    r = request.get_json()
    
    distance = distance.euclidean(r["a"], r["b"]) 

    dist = {
        "distance": "Distance is {0}".format(distance),
	"a": "a is {0}".format(r["a"]),
	"b": "b is {0}".format(r["b"])
    }
    return jsonify(dist)
