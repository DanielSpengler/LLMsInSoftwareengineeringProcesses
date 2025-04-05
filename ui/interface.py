import tkinter as tk
from tkinter import scrolledtext, ttk
import chat.chat_model as chat_model
import logging
from chat.chat_model import ChatMode

def send_message(chat_display, mode, entry):
    user_message = entry.get()
    if user_message:
        logging.info(f"Message received: {user_message}")
        chat_display.insert(tk.END, f'You: {user_message}\n')
        entry.delete(0, tk.END)
        # Simple response for demonstration
        # chat_display.insert(tk.END, f'Bot: Echoing - {user_message}\n')
        # TODO : Integrate with actual chat model
        response = chat_model.get_response(mode, user_message)
        chat_display.insert(tk.END, f'Bot: {response}\n')
        chat_display.see(tk.END)

def create_chat_tab(tab, mode):
    frame = ttk.Frame(tab)
    tab.add(frame, text=mode.value)

    chat_display = scrolledtext.ScrolledText(frame, wrap=tk.WORD, state='normal')
    chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    entry = tk.Entry(frame, width=50)
    entry.pack(padx=10, pady=5)
    send_button = tk.Button(frame, text='Send', command=lambda: send_message(chat_display, mode, entry))
    send_button.pack(pady=5)
    entry.bind('<Return>', lambda event: send_message(chat_display, mode, entry))  # Fixed line

    return chat_display, entry

def start_chat_interface():
    global root
    root = tk.Tk()
    root.title('Chat Interface')
    root.geometry('400x500')
    logging.info("Chat Interface started.")

    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=1, fill='both')

    # Create two tabs for two chats
    chat_display1, entry1 = create_chat_tab(tab_control, ChatMode.REQUIREMENTS)
    chat_display2, entry2 = create_chat_tab(tab_control, ChatMode.CODE_GENERATION)

    root.mainloop()