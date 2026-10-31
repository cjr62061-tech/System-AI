from flask import Flask, request, jsonify, render_template_string
from ai_brain import SuperAI

app = Flask(__name__)
ai = SuperAI()

HTML = """
<h1>Bhai Ka Super AI</h1>
<input id="msg" placeholder="Kuch bol bhai..."><button onclick="send()">Bhej</button>
<p id="reply"></p>
<script>
function send(){
 fetch('/chat', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({message:document.getElementById('msg').value})})
 .then(r=>r.json()).then(d=>document.getElementById('reply').innerText=d.reply)
}
</script>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json.get("message", "")
    return jsonify({"reply": ai.chat(msg)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)