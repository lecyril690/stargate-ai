import { useState } from "react"

export default function StargateAIInterface() {
  const [messages, setMessages] = useState([
    { role: "ai", text: "Stargate Core initialisé." }
  ])
  const [input, setInput] = useState("")

async function send() {
  if (!input) return

  const userMessage = input

  setMessages(prev => [
    ...prev,
    { role: "user", text: userMessage }
  ])

  setInput("")

  const res = await fetch("https://stargate-backend-ynld.onrender.com/chat", {", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      text: userMessage,
    }),
  })

  const data = await res.json()

  setMessages(prev => [
    ...prev,
    { role: "ai", text: data.reply }
  ])
}

  return (
    <div style={{
      height: "100vh",
      background: "black",
      color: "cyan",
      fontFamily: "monospace",
      padding: 20
    }}>
      <h1>STARGATE AI CORE</h1>

      <div style={{ height: "70vh", overflow: "auto", border: "1px solid cyan", padding: 10 }}>
        {messages.map((m, i) => (
          <div key={i} style={{ margin: "10px 0" }}>
            <b>{m.role}:</b> {m.text}
          </div>
        ))}
      </div>

      <div style={{ marginTop: 10 }}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          style={{ width: "80%" }}
        />
        <button onClick={send}>SEND</button>
      </div>
    </div>
  )
}
