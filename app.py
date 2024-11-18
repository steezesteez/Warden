
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace this with your target API URL
API_URL = "https://api.example.com/endpoint"

@app.route("/")
def home():
    return "Welcome to Warden's Threshold - Your Autonomous Chatbot Gateway!"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Call external API
    try:
        response = requests.get(API_URL, params={"query": user_message})
        response_data = response.json()
        bot_reply = response_data.get("reply", "I couldn't process that.")
    except Exception as e:
        return jsonify({"error": f"API request failed: {str(e)}"}), 500

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
