from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    return "Market Intelligence Backend is running"


@app.route("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "message": "Market Intelligence backend is running"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
