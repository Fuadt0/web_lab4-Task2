from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "API is running",
        "endpoints": ["/api/hello"]
    })

@app.route("/hello")
def hello():
    return jsonify({
        "message": "Hello from Flask!",
        "status": "success"
    })