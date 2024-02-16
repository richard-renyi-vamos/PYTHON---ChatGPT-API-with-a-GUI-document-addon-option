import tkinter as tk
from tkinter import filedialog, messagebox
import requests

# Function to send text to ChatGPT API
def send_to_chatgpt(text):
    url = "https://api.openai.com/v1/completions"
    payload = {
        "model": "text-davinci-003",
        "prompt": text,
        "max_tokens": 50
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY"  # Replace YOUR_API_KEY with your actual API key
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()["choices"][0]["text"].strip()

# Function to open a file dialog and select a document
def select_document():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        with open(file_path, "rb") as file:
            # Perform processing on the selected document if needed
            pass
        messagebox.showinfo("Document Selected", "Document selected successfully!")

# Function to handle sending text to ChatGPT
def send_message():
    user_input = user_input_text.get("1.0", tk.END).strip()
    if user_input:
        chat_history_text.config(state=tk.NORMAL)
        chat_history_text.insert(tk.END, "You: " + user_input + "\n")
        chat_history_text.insert(tk.END, "ChatGPT: " + send_to_chatgpt(user_input) + "\n\n")
        chat_history_text.config(state=tk.DISABLED)
        user_input_text.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a message!")

# Create the main window
root = tk.Tk()
root.title("ChatGPT GUI")

# Create GUI elements
user_input_label = tk.Label(root, text="Enter your message:")
user_input_label.pack(pady=10)

user_input_text = tk.Text(root, height=3, width=50)
user_input_text.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

chat_history_text = tk.Text(root, height=20, width=50)
chat_history_text.pack(pady=10)
chat_history_text.config(state=tk.DISABLED)

document_button = tk.Button(root, text="Select Document", command=select_document)
document_button.pack(pady=5)

# Run the GUI application
root.mainloop()
