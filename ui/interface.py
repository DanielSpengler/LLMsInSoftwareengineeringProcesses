import tkinter as tk
from tkinter import scrolledtext, ttk
import chat.chat_model as chat_model
from chat.chat_model import ChatMode
import logging

# Configuration
WINDOW_TITLE = "Chat Interface"
WINDOW_SIZE = "400x500"
DEFAULT_CHAT_DISPLAY_HEIGHT = 15

def create_dropdown(parent, label_text, options, default_value):
    frame = tk.Frame(parent)
    frame.pack(padx=10, pady=5, anchor='w', fill=tk.X)

    label = tk.Label(frame, text=label_text)
    label.pack(side=tk.LEFT, padx=(0, 5), pady=5)

    selected_value = tk.StringVar(value=default_value)
    dropdown = ttk.Combobox(frame, textvariable=selected_value, values=options, state="readonly")
    dropdown.pack(side=tk.LEFT, pady=5)

    return selected_value

def create_chat_display(parent, height=DEFAULT_CHAT_DISPLAY_HEIGHT):
    chat_display = scrolledtext.ScrolledText(parent, wrap=tk.WORD, state='normal', height=height)
    chat_display.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
    return chat_display

def send_message(chat_display, mode, entry, selected_model):
    user_message = entry.get().strip()
    if not user_message:
        # ignore empty messages
        return

    # FIXME Remove this log after testing
    logging.info(f"Message received: {user_message}")
    chat_display.insert(tk.END, f'You: {user_message}\n')
    entry.delete(0, tk.END)

    logging.info(f"Using chat model: {selected_model.get()}")
    response = chat_model.get_response(mode, selected_model.get(), user_message)
    chat_display.insert(tk.END, f'Bot: {response}\n')
    chat_display.see(tk.END)

def create_chat_tab(tab_control, mode):
    frame = ttk.Frame(tab_control)
    tab_control.add(frame, text=mode.value)

    # Get possible chat models based on the mode
    model_options = chat_model.get_possible_chat_models(mode)
    selected_model = create_dropdown(frame, "Select Model:", model_options, model_options[0])

    # Chat display area
    chat_display = create_chat_display(frame)

    # Add welcome message
    chat_display.insert(tk.END, f'Bot: {chat_model.get_welcome_message(mode)}\n')

    # Input frame with entry and send button
    input_frame = tk.Frame(frame)
    input_frame.pack(padx=10, pady=5, fill=tk.X)

    entry = tk.Entry(input_frame, width=40)
    entry.pack(side=tk.LEFT, padx=(0, 5), pady=5)

    send_button = tk.Button(input_frame, text='Send', command=lambda: send_message(chat_display, mode, entry, selected_model))
    send_button.pack(side=tk.LEFT, pady=5)

    entry.bind('<Return>', lambda event: send_message(chat_display, mode, entry, selected_model))

    return chat_display, entry

def start_chat_interface():
    root = tk.Tk()
    root.title(WINDOW_TITLE)
    root.geometry(WINDOW_SIZE)

    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=1, fill='both')

    # Create tabs for each chat mode
    # ChatMode.values()  # Ensure all modes are loaded
    chat_modes = [ChatMode.REQUIREMENTS, ChatMode.CODE_GENERATION]
    for mode in ChatMode:
        create_chat_tab(tab_control, mode)

    root.mainloop()