from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running successfully"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data["message"]

    reply = "You said: " + user_message

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()
