from flask import Flask, render_template, request, jsonify
from chatbot import FAQChatbot
import os

app = Flask(__name__)

#Start chatbot
kb_path = os.getenv("KB_PATH", "knowledge_base.csv")
bot = FAQChatbot(kb_path=kb_path)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    question = ""
    if request.method == "POST":
        question = request.form.get("question", "")
        answer = bot.get_answer(question)
    return render_template("index.html", question=question, answer=answer)

@app.route("/api/ask", methods=["POST"])
def api_ask():
    data = request.get_json(force=True)
    question = data.get("question", "")
    answer = bot.get_answer(question)
    return jsonify({"answer": answer})

@app.route("/upload_kb", methods=["POST"])
def upload_kb():
    #Support KB CSV upload
    if "file" not in request.files:
        return "No file provided", 400
    file = request.files["file"]
    path = os.path.join("uploaded_kb.csv")
    file.save(path)
    try:
        bot.reload_kb(path)
    except Exception as e:
        return f"Error loading new KB: {e}", 400
    return "Knowledge base updated!", 200

if __name__ == "__main__":
    app.run(debug=True)
