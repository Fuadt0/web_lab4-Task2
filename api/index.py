from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "message": "API is running",
        "endpoints": ["/api/hello"]
    })

@app.get("/hello")
def hello():
    return jsonify({
        "message": "Hello from Flask!",
        "status": "success"
    })