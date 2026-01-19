from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api")
def home():
    return jsonify({"message": "API is running", "endpoints": ["/api/hello"]})

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask!", "status": "success"})