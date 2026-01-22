from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "AI Welfare Backend Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    income = data.get("income")
    family_size = data.get("family_size")

    # Simple logic (replace with ML later)
    if income < 10000:
        result = "Eligible for Welfare"
    else:
        result = "Not Eligible"

    return jsonify({"result": result})

if __name__ == "__main__
