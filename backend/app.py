from flask import Flask, request, jsonify
from flask_cors import CORS

import numpy as np
import pickle
import json
import tensorflow as tf
import random

# ✅ CREATE FLASK APP
app = Flask(__name__)
CORS(app)   # enable CORS

# Load model and files
model = tf.keras.models.load_model("chatbot_model.h5")
classes = np.load("classes.npy")

with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

responses = {intent["tag"]: intent["responses"] for intent in data["intents"]}

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

CONFIDENCE_THRESHOLD = 0.5

def get_reply(msg):
    x = vectorizer.transform([msg]).toarray()
    predictions = model.predict(x, verbose=0)[0]

    max_prob = np.max(predictions)
    tag_index = np.argmax(predictions)
    tag = classes[tag_index]

    if max_prob < CONFIDENCE_THRESHOLD:
        return "Sorry, I didn't understand that. Can you rephrase? 🤔"

    return random.choice(responses[tag])


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()   # ✅ correct
    user_msg = data.get("message", "")
    reply = get_reply(user_msg)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
