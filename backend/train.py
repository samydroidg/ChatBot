# ==============================
# AI Chatbot Training Script
# ==============================

import json
import numpy as np
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

from keras.models import Sequential
from keras.layers import Dense, Dropout


# ------------------------------
# Load intents data
# ------------------------------
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

patterns = []
tags = []
responses = {}

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])
    responses[intent["tag"]] = intent["responses"]


# ------------------------------
# Text Vectorization
# ------------------------------
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns).toarray()

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(tags)


# ------------------------------
# Build Neural Network Model
# ------------------------------
model = Sequential()
model.add(Dense(128, input_shape=(X.shape[1],), activation="relu"))
model.add(Dropout(0.2))
model.add(Dense(64, activation="relu"))
model.add(Dense(len(set(tags)), activation="softmax"))

model.compile(
    loss="sparse_categorical_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)


# ------------------------------
# Train Model
# ------------------------------
model.fit(X, np.array(y), epochs=500, verbose=1)


# ------------------------------
# Save Model & Files
# ------------------------------
model.save("chatbot_model.h5")
np.save("classes.npy", label_encoder.classes_)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model training complete!")
print("✅ Files saved: chatbot_model.h5, classes.npy, vectorizer.pkl")
