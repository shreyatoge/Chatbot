from flask import Flask, request, jsonify

app = Flask(__name__)

qa = {
"what is a bank":"A bank is a financial institution that accepts deposits and provides loans.",
"savings account":"Savings account helps you save money safely.",
"loan types":"Home, car, personal, education loans available.",
"what is upi":"UPI is instant payment system."
}

@app.route("/")
def home():
    return "Bank Chatbot Running"

@app.route("/chat", methods=["POST"])
def chat():
    user = request.json["message"].lower()

    reply = "Please ask banking question."

    for q in qa:
        if q in user:
            reply = qa[q]
            break

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()