import tkinter as tk
from tkinter import filedialog
import requests
import pyttsx3

def select_file():
    file_path = filedialog.askopenfilename()
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, file_path)

def send_message():
    user_input = entry.get()
    use_local_file = use_file_var.get()
    additional_info = ""
    
    if use_local_file:
        file_path = file_path_entry.get()
        additional_info = get_additional_info_from_file(file_path)

    response = requests.post('http://your-api-endpoint', json={'message': user_input, 'additional_info': additional_info})
    response_text = response.json()['response']
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, "You: " + user_input + "\n")
    output_text.insert(tk.END, "ChatGPT: " + response_text + "\n")
    output_text.config(state=tk.DISABLED)
    entry.delete(0, tk.END)
    
    if read_aloud_var.get():
        engine.say(response_text)
        engine.runAndWait()

def get_additional_info_from_file(file_path):
    # Read data from the selected file
    # This function should return the relevant information from the file
    # You can implement your own logic to read and process the file
    pass

# Create GUI window
root = tk.Tk()
root.title("ChatGPT")

# Create widgets
entry = tk.Entry(root, width=50)
use_file_var = tk.BooleanVar()
use_file_checkbox = tk.Checkbutton(root, text="Use Local File", variable=use_file_var)
file_path_entry = tk.Entry(root, width=50)
select_file_button = tk.Button(root, text="Select File", command=select_file)
read_aloud_var = tk.BooleanVar()
read_aloud_checkbox = tk.Checkbutton(root, text="Read Aloud", variable=read_aloud_var)
send_button = tk.Button(root, text="Send", command=send_message)
output_text = tk.Text(root, wrap=tk.WORD, width=60, height=20)
output_text.config(state=tk.DISABLED)

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Layout widgets
entry.pack(pady=10)
use_file_checkbox.pack()
file_path_entry.pack(pady=5)
select_file_button.pack()
read_aloud_checkbox.pack()
send_button.pack()
output_text.pack(pady=10)

# Run the GUI
root.mainloop()
