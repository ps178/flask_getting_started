import math
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
    
    distance = math.sqrt(((r["b"][0]-r["a"][0])*(r["b"][0]-r["a"][0]))+((r["b"][1]-r["a"][1])*(r["b"][1]-r["a"][1])))

    dist = {
        "distance": "Distance is {0}".format(distance),
	"a": "a is {0}".format(r["a"]),
	"b": "b is {0}".format(r["b"])
    }
    return jsonify(dist)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
