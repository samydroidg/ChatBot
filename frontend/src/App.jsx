import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!message.trim()) return;

    const userMsg = { sender: "user", text: message };
    setChat((prev) => [...prev, userMsg]);
    setLoading(true);

    try {
      const res = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message }),
      });

      const data = await res.json();

      const botMsg = { sender: "bot", text: data.reply };
      setChat((prev) => [...prev, botMsg]);
    } catch (err) {
      setChat((prev) => [
        ...prev,
        { sender: "bot", text: "Server not responding 😕" },
      ]);
    }

    setMessage("");
    setLoading(false);
  };

  const handleKey = (e) => {
    if (e.key === "Enter") sendMessage();
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>🤖 AI Chatbot</h2>

      <div style={styles.chatBox}>
        {chat.map((msg, index) => (
          <div
            key={index}
            style={{
              ...styles.message,
              alignSelf: msg.sender === "user" ? "flex-end" : "flex-start",
              background:
                msg.sender === "user" ? "#4f46e5" : "#1f2937",
            }}
          >
            {msg.text}
          </div>
        ))}

        {loading && (
          <div style={{ ...styles.message, alignSelf: "flex-start" }}>
            Typing...
          </div>
        )}
      </div>

      <div style={styles.inputBox}>
        <input
          type="text"
          placeholder="Ask something..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={handleKey}
          style={styles.input}
        />
        <button onClick={sendMessage} style={styles.button}>
          Send
        </button>
      </div>
    </div>
  );
}

const styles = {
  container: {
    maxWidth: "600px",
    margin: "40px auto",
    fontFamily: "sans-serif",
    display: "flex",
    flexDirection: "column",
    height: "90vh",
  },
  title: {
    textAlign: "center",
  },
  chatBox: {
    flex: 1,
    border: "1px solid #333",
    padding: "10px",
    borderRadius: "8px",
    overflowY: "auto",
    display: "flex",
    flexDirection: "column",
    gap: "8px",
    background: "#111",
    color: "#fff",
  },
  message: {
    padding: "10px",
    borderRadius: "6px",
    maxWidth: "70%",
  },
  inputBox: {
    display: "flex",
    gap: "10px",
    marginTop: "10px",
  },
  input: {
    flex: 1,
    padding: "10px",
    borderRadius: "6px",
    border: "1px solid #333",
  },
  button: {
    padding: "10px 16px",
    borderRadius: "6px",
    border: "none",
    background: "#22c55e",
    cursor: "pointer",
    fontWeight: "bold",
  },
};

export default App;
