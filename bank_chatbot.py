import tkinter as tk
from tkinter import scrolledtext, messagebox

# ---------------- USER DATA ---------------- #
USER_DATA = {
    "username": "shreya",
    "password": "1234",
    "balance": 50000
}

# ---------------- 100 BANK QUESTIONS ---------------- #
qa = {

# General Banking (1–10)
"what is a bank":"A bank is a financial institution that accepts deposits and provides loans.",
"bank services":"We provide accounts, loans, cards and digital banking services.",
"working hours":"Bank working hours are 10 AM to 4 PM (Mon-Fri).",
"bank location":"We have branches across India.",
"customer care":"Call 1800-123-456.",
"ifsc code":"IFSC code is printed on your cheque book.",
"swift code":"Contact branch for SWIFT code details.",
"bank holidays":"Check official website for holidays.",
"update details":"Visit branch with ID proof.",
"branch finder":"Use branch locator on website.",

# Savings (11–25)
"savings account":"Savings account helps you save money safely.",
"minimum balance":"Minimum balance required is ₹1000.",
"open savings account":"Aadhaar and PAN required.",
"savings interest rate":"Interest rate is 4% per year.",
"zero balance":"Zero balance account available.",
"check balance":"Use ATM or mobile banking.",
"download statement":"Download from internet banking.",
"close savings account":"Submit closure form at branch.",
"joint account":"Joint account facility available.",
"add nominee":"Nominee can be added at branch.",
"update mobile":"Update mobile number with ID proof.",
"change address":"Submit address proof at branch.",
"passbook":"Passbook available.",
"deposit limit":"Depends on account type.",
"account statement":"Statement available online.",

# Current (26–40)
"current account":"Current account mainly for business.",
"open current account":"Submit business documents.",
"current minimum balance":"Varies by account type.",
"overdraft":"Overdraft facility available.",
"activate overdraft":"Apply at branch.",
"current charges":"Charges depend on account type.",
"upi for current":"UPI can be linked.",
"current statement":"Download via net banking.",
"close current":"Submit request at branch.",
"cheque book":"Cheque book available.",
"request cheque":"Request via net banking.",
"cheque clearing":"2-3 working days.",
"stop cheque":"Stop cheque via net banking.",
"stop payment":"Provide cheque number.",
"business account":"Business accounts available.",

# Loans (41–55)
"loan types":"Home, car, personal, education loans available.",
"home loan":"Home loan up to ₹50 lakhs.",
"home loan interest":"Interest starts from 8%.",
"home documents":"Income and ID proof required.",
"car loan":"Car loan with flexible EMI.",
"personal loan":"Personal loan up to ₹10 lakhs.",
"education loan":"Education loan for students.",
"emi":"EMI based on interest and tenure.",
"loan tenure":"Up to 20 years.",
"loan prepayment":"Allowed with charges.",
"loan foreclosure":"Allowed as per policy.",
"processing fee":"Processing fee applicable.",
"loan status":"Check status online.",
"business loan":"Business loan available.",
"gold loan":"Gold loan with quick approval.",

# Cards (56–70)
"apply credit card":"Apply online or at branch.",
"credit limit":"Depends on income.",
"block debit card":"Call customer care immediately.",
"change atm pin":"Change PIN at ATM.",
"annual fee":"Depends on card type.",
"increase credit limit":"Request via mobile app.",
"activate card":"Activate via SMS.",
"reward points":"Earn points on purchases.",
"redeem reward":"Redeem via app.",
"international usage":"Enable from app.",
"contactless":"Tap card to pay.",
"card statement":"Download from app.",
"credit card emi":"Convert purchase to EMI.",
"report fraud":"Report immediately.",
"close credit card":"Submit closure request.",

# Digital Banking (71–85)
"internet banking":"Register online.",
"reset password":"Use forgot password option.",
"mobile banking":"Download and register.",
"what is upi":"UPI is instant payment system.",
"create upi":"Create in mobile app.",
"neft":"NEFT during banking hours.",
"rtgs":"RTGS for high amount transfer.",
"imps":"IMPS works 24/7.",
"transaction limit":"Daily limit ₹1 lakh.",
"bill payment":"Pay bills online.",
"mobile recharge":"Recharge via app.",
"fastag":"FASTag recharge available.",
"scan qr":"Scan QR to pay.",
"link aadhaar":"Link at branch.",
"link pan":"Link PAN to account.",

# Security (86–100)
"otp":"Never share OTP.",
"kyc":"Complete KYC for services.",
"kyc documents":"Aadhaar and PAN required.",
"secure login":"Use strong password.",
"two factor":"Enabled for security.",
"privacy policy":"Available on website.",
"grievance":"Contact grievance officer.",
"feedback":"We value feedback.",
"complaint":"Register complaint online.",
"atm complaint":"Report ATM issue.",
"lost card":"Block immediately.",
"cyber crime":"Report on cyber crime portal.",
"fraud protection":"Bank provides fraud monitoring.",
"data security":"Your data is encrypted.",
"customer support":"24/7 customer support available."
}

# ---------------- LOGIN WINDOW ---------------- #
def login():
    if username_entry.get() == USER_DATA["username"] and password_entry.get() == USER_DATA["password"]:
        login_window.destroy()
        open_chatbot()
    else:
        messagebox.showerror("Error", "Invalid Login!")

login_window = tk.Tk()
login_window.title("Login - Bank Chatbot")
login_window.geometry("300x250")

tk.Label(login_window, text="Username").pack(pady=5)
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password").pack(pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", command=login).pack(pady=20)

# ---------------- MAIN CHATBOT ---------------- #
def open_chatbot():
    global chat_area, entry, balance_label

    window = tk.Tk()
    window.title("🏦 Ultimate Bank Chatbot")
    window.geometry("800x600")
    window.configure(bg="#1e1e1e")

    sidebar = tk.Frame(window, bg="#2b2b2b", width=150)
    sidebar.pack(side=tk.LEFT, fill=tk.Y)

    balance_label = tk.Label(sidebar, text=f"Balance:\n₹{USER_DATA['balance']}",
                             fg="white", bg="#2b2b2b")
    balance_label.pack(pady=20)

    tk.Button(sidebar, text="Check Balance", width=15,
              command=check_balance).pack(pady=5)

    tk.Button(sidebar, text="Deposit ₹1000", width=15,
              command=deposit_money).pack(pady=5)

    tk.Button(sidebar, text="Withdraw ₹1000", width=15,
              command=withdraw_money).pack(pady=5)

    tk.Button(sidebar, text="Clear Chat", width=15,
              command=lambda: chat_area.delete("1.0", tk.END)).pack(pady=5)

    chat_frame = tk.Frame(window, bg="#1e1e1e")
    chat_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    chat_area = scrolledtext.ScrolledText(chat_frame,
                                          bg="#252526",
                                          fg="white",
                                          font=("Arial", 11))
    chat_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    bottom_frame = tk.Frame(chat_frame, bg="#1e1e1e")
    bottom_frame.pack(pady=10)

    entry = tk.Entry(bottom_frame, width=50, font=("Arial", 12))
    entry.grid(row=0, column=0, padx=10)
    entry.bind("<Return>", send_message)

    tk.Button(bottom_frame, text="Send", command=send_message,
              bg="#007acc", fg="white").grid(row=0, column=1)

    window.mainloop()

# ---------------- FUNCTIONS ---------------- #
def send_message(event=None):
    user_input = entry.get().lower()
    if not user_input:
        return

    chat_area.insert(tk.END, f"\nYou: {user_input}\n")

    response = "Please ask banking related question."

    for question in qa:
        if question in user_input:
            response = qa[question]
            break

    chat_area.insert(tk.END, f"Bot: {response}\n")
    chat_area.yview(tk.END)
    entry.delete(0, tk.END)

def check_balance():
    chat_area.insert(tk.END, f"\nBot: Your balance is ₹{USER_DATA['balance']}\n")

def deposit_money():
    USER_DATA["balance"] += 1000
    balance_label.config(text=f"Balance:\n₹{USER_DATA['balance']}")
    chat_area.insert(tk.END, "\nBot: ₹1000 Deposited Successfully\n")

def withdraw_money():
    if USER_DATA["balance"] >= 1000:
        USER_DATA["balance"] -= 1000
        balance_label.config(text=f"Balance:\n₹{USER_DATA['balance']}")
        chat_area.insert(tk.END, "\nBot: ₹1000 Withdrawn Successfully\n")
    else:
        chat_area.insert(tk.END, "\nBot: Insufficient Balance\n")

login_window.mainloop()
