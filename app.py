from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "message": "API is running",
        "endpoints": ["/hello"]
    })

@app.get("/hello")
def hello():
    return jsonify({
        "message": "Hello from Flask!",
        "status": "success"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)