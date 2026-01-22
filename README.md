# 🤖 AI Chatbot – Setup & Usage Guide

This project is a full-stack AI chatbot using **Flask + TensorFlow** for the backend and **React (Vite)** for the frontend.

---

## ⚙️ Requirements

- Python 3.9+
- Node.js 18+
- npm
- Git

---

## ▶️ Backend Setup & Run

### 1️⃣ Go to backend directory
```
cd backend
```

### 2️⃣ Create virtual environment
```
python -m venv tfenv
```

Activate it:

Windows

```
tfenv\Scripts\activate
```


Linux / Mac
```
source tfenv/bin/activate
```

### 3️⃣ Install backend dependencies
```
pip install flask flask-cors tensorflow numpy scikit-learn
```

### 4️⃣ Train the chatbot model
```
python train.py
```


#### This will generate:

-- chatbot_model.h5

-- classes.npy

-- vectorizer.pkl

### 5️⃣ Start backend server
```
python app.py
```


Backend will run at:

```
http://127.0.0.1:5000
```

## ▶️ Frontend Setup & Run
### 6️⃣ Go to frontend directory
```
cd ../frontend
```

### 7️⃣ Install frontend dependencies
```
npm install
```

### 8️⃣ Start frontend
```
npm run dev
```

Frontend will run at:

```
http://localhost:5173
```

## 💬 How to Use the Chatbot

- Start the backend server

- Start the frontend app

- Open http://localhost:5173 in your browser

- Type a message in the input box

- Press Enter or click Send

- Chatbot will reply instantly

## ⚠️ Important Notes

- Backend must be running before frontend

- Train the model before starting backend

- If backend is not running, frontend will show:

```
Server not responding 😕
```
