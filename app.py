from flask import Flask, request, jsonify, render_template
from chatbot import get_bot_response

app = Flask(__name__)


def save_chat_log(user_message, bot_response):
    """
    Menyimpan riwayat percakapan ke file txt.
    """
    with open("logs/chat_log.txt", "a", encoding="utf-8") as file:
        file.write(f"User: {user_message}\n")
        file.write(f"Bot: {bot_response}\n\n")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    user_message = data.get("message", "")

    # Ambil respon chatbot
    bot_response = get_bot_response(user_message)

    # Simpan log percakapan
    save_chat_log(user_message, bot_response)

    return jsonify({
        "response": bot_response
    })


if __name__ == "__main__":
    app.run(debug=True)