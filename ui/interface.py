import tkinter as tk
from tkinter import scrolledtext

def send_message():
    user_message = entry.get()
    if user_message:
        chat_display.insert(tk.END, f'You: {user_message}\n')
        entry.delete(0, tk.END)
        # Simple response for demonstration
        chat_display.insert(tk.END, f'Bot: Echoing - {user_message}\n')


def start_chat_interface():
    global root, chat_display, entry
    root = tk.Tk()
    root.title('Chat Interface')
    root.geometry('400x500')

    chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='normal')
    chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    entry = tk.Entry(root, width=50)
    entry.pack(padx=10, pady=5)
    entry.bind('<Return>', lambda event: send_message())

    send_button = tk.Button(root, text='Send', command=send_message)
    send_button.pack(pady=5)

    root.mainloop()