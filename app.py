import os
from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timezone

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Market Intelligence Backend is running"

@app.route("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "message": "Market Intelligence API is working"
    })

@app.route("/api/market-data")
def market_data():

    # DEMO DATA ONLY
    # This is NOT live NSE/BSE data.
    # It will be replaced with an authorized data source later.

    data = {
        "source": "DEMO",
        "live": False,
        "timestamp": datetime.now(timezone.utc).isoformat(),

        "market": {
            "name": "NIFTY 50",
            "value": 25000.00,
            "change": 125.50,
            "change_percent": 0.50
        },

        "stocks": [
            {
                "symbol": "RELIANCE",
                "price": 1500.00,
                "change_percent": 1.20
            },
            {
                "symbol": "TCS",
                "price": 3200.00,
                "change_percent": -0.40
            },
            {
                "symbol": "INFY",
                "price": 1600.00,
                "change_percent": 0.75
            }
        ]
    }

    return jsonify(data)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
