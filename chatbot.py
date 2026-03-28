import tkinter as tk
from tkinter import scrolledtext

# -------- Product Data --------
products = {
    "punjabi": {
        "price": "Starting from 1200 BDT",
        "location": "Available all over Bangladesh",
        "details": "High quality cotton Punjabi for men."
    },
    "shirt": {
        "price": "Starting from 800 BDT",
        "location": "Available in Dhaka",
        "details": "Stylish casual shirts."
    }
}

# -------- Chatbot Logic --------
def chatbot_response(user_input):
    user_input = user_input.lower()

    for product in products:
        if product in user_input:
            if "price" in user_input:
                return f"{product.title()} price: {products[product]['price']}"
            elif "location" in user_input:
                return f"{product.title()} location: {products[product]['location']}"
            else:
                return f"{product.title()}: {products[product]['details']}"

    if "hi" in user_input or "hello" in user_input:
        return "Hello! How can I help you today?"

    return "Sorry, I didn't understand. Ask about products, price, or location."


# -------- Send Message --------
def send_message(event=None):   # <-- important (event added)
    user_msg = entry.get()

    if user_msg.strip() == "":
        return

    chat_box.insert(tk.END, "You: " + user_msg + "\n")

    bot_reply = chatbot_response(user_msg)
    chat_box.insert(tk.END, "Bot: " + bot_reply + "\n\n")

    entry.delete(0, tk.END)
    chat_box.see(tk.END)


# -------- UI Setup --------
root = tk.Tk()
root.title("Shopping Chatbot")
root.geometry("500x500")

chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(padx=10, pady=5, fill=tk.X)

entry.focus()   # <-- VERY IMPORTANT

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack(pady=5)

# -------- Enter Key Binding --------
entry.bind("<Return>", send_message)   # <-- FIXED WAY

# -------- Run App --------
root.mainloop()