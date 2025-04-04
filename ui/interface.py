import tkinter as tk
from tkinter import scrolledtext
import chat.chat_model as chat_model
import logging

def send_message():
    user_message = entry.get()
    if user_message:
        logging.info(f"Message received: {user_message}")
        chat_display.insert(tk.END, f'You: {user_message}\n')
        entry.delete(0, tk.END)
        # Simple response for demonstration
        # chat_display.insert(tk.END, f'Bot: Echoing - {user_message}\n')
        # TODO : Integrate with actual chat model
        response = chat_model.get_response(user_message)
        chat_display.insert(tk.END, f'Bot: {response}\n')
        chat_display.see(tk.END)
        
        


def start_chat_interface():
    global root, chat_display, entry
    root = tk.Tk()
    root.title('Chat Interface')
    root.geometry('400x500')
    logging.info("Chat Interface started.")

    chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='normal')
    chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    entry = tk.Entry(root, width=50)
    entry.pack(padx=10, pady=5)
    entry.bind('<Return>', lambda event: send_message())

    send_button = tk.Button(root, text='Send', command=send_message)
    send_button.pack(pady=5)

    root.mainloop()