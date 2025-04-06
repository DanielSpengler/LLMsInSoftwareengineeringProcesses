import tkinter as tk
from tkinter import scrolledtext, ttk
import chat.chat_model as chat_model
import logging
from chat.chat_model import ChatMode

def send_message(chat_display, mode, entry, selected_model):
    user_message = entry.get()
    if user_message:
        logging.info(f"Message received: {user_message}")
        chat_display.insert(tk.END, f'You: {user_message}\n')
        entry.delete(0, tk.END)
        # Use the selected model for response
        logging.info(f"Using chat model: {selected_model.get()}")
        response = chat_model.get_response(mode, selected_model.get(), user_message)
        chat_display.insert(tk.END, f'Bot: {response}\n')
        chat_display.see(tk.END)

def create_chat_tab(tab, mode):
    frame = ttk.Frame(tab)
    tab.add(frame, text=mode.value)

    # Frame for label and dropdown menu
    model_frame = tk.Frame(frame)
    model_frame.pack(padx=10, pady=5, anchor='w', fill=tk.X)

    # Dropdown menu for selecting chat model
    model_label = tk.Label(model_frame, text="Select Model:")
    model_label.pack(side=tk.LEFT, padx=(0, 5), pady=5)

    model_options = ["Model A", "Model B", "Model C"]  # Example models
    selected_model = tk.StringVar(value=model_options[0])
    model_dropdown = ttk.Combobox(model_frame, textvariable=selected_model, values=model_options, state="readonly")
    model_dropdown.pack(side=tk.LEFT, pady=5)

    # Chat display area (scaled down)
    chat_display = scrolledtext.ScrolledText(frame, wrap=tk.WORD, state='normal', height=15)  # Reduced height
    chat_display.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

    # Frame for entry and send button
    input_frame = tk.Frame(frame)
    input_frame.pack(padx=10, pady=5, fill=tk.X)

    entry = tk.Entry(input_frame, width=40)
    entry.pack(side=tk.LEFT, padx=(0, 5), pady=5)

    send_button = tk.Button(input_frame, text='Send', command=lambda: send_message(chat_display, mode, entry, selected_model))
    send_button.pack(side=tk.LEFT, pady=5)

    entry.bind('<Return>', lambda event: send_message(chat_display, mode, entry, selected_model))

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