import tkinter as tk
from tkinter import scrolledtext

# ---------------- BANK QUESTIONS DATABASE ---------------- #
qa = {

# General Banking
"what is a bank":"A bank is a financial institution that accepts deposits and provides loans.",
"working hours":"Our working hours are 10 AM to 4 PM (Monday to Friday).",
"customer care":"Call 1800-123-456 for customer support.",
"ifsc code":"IFSC code is printed on your cheque book.",
"swift code":"Contact branch for SWIFT code details.",

# Savings Account
"what is savings account":"Savings account helps you save money safely and earn interest.",
"minimum balance":"Minimum balance required is ₹1000.",
"open savings account":"You need Aadhaar, PAN and passport size photo.",
"savings interest rate":"Interest rate is 4% per year.",
"check balance":"Use ATM, mobile banking or internet banking.",

# Current Account
"what is current account":"Current account is mainly for business transactions.",
"overdraft facility":"Yes, overdraft facility is available.",
"cheque book":"Cheque book is available on request.",
"stop cheque":"You can stop cheque using net banking.",

# Loans
"loan types":"We provide home loan, car loan, personal loan and education loan.",
"home loan interest":"Home loan interest starts from 8%.",
"personal loan":"Personal loan available up to ₹10 lakhs.",
"emi calculation":"EMI depends on loan amount, tenure and interest rate.",

# Cards
"apply credit card":"You can apply online or at branch.",
"block debit card":"Call customer care immediately to block card.",
"change atm pin":"Change ATM PIN at any ATM machine.",
"reward points":"You earn reward points on every purchase.",

# Digital Banking
"what is upi":"UPI is instant money transfer system.",
"create upi id":"Create UPI ID using mobile banking app.",
"neft":"NEFT transfers are available during banking hours.",
"imps":"IMPS works 24/7.",
"transaction limit":"Daily transaction limit is ₹1 lakh.",

# Security
"report fraud":"Immediately contact customer care.",
"otp":"Never share your OTP with anyone.",
"kyc":"Complete KYC to continue banking services.",
"lost card":"Block your card immediately using mobile app."
}

# ---------------------------------------------------------- #

def send_message():
    user_input = entry.get().lower()
    chat_area.insert(tk.END, "You: " + user_input + "\n")

    response = "Sorry, I don't understand. Please ask banking related question."

    for question in qa:
        if question in user_input:
            response = qa[question]
            break

    chat_area.insert(tk.END, "Bot: " + response + "\n\n")
    entry.delete(0, tk.END)

def exit_app():
    window.destroy()

# ---------------- GUI DESIGN ---------------- #

window = tk.Tk()
window.title("🏦 Bank Chatbot App")
window.geometry("500x600")
window.configure(bg="lightblue")

chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=25)
chat_area.pack(pady=10)

entry = tk.Entry(window, width=40)
entry.pack(pady=5)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=5)

exit_button = tk.Button(window, text="Exit", command=exit_app, bg="red")
exit_button.pack(pady=5)

window.mainloop()