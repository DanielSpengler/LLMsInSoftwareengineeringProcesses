import tkinter as tk
from tkinter import scrolledtext, ttk
import chat.chat_model as chat_model
import export.export_utility as export_util
from chat.chat_model import ChatMode
import logging

# Configuration
WINDOW_TITLE = "Chat Interface"
WINDOW_SIZE = "400x500"
DEFAULT_CHAT_DISPLAY_HEIGHT = 15

class ScrollableTextWithButtons(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)

        # Create a canvas and scrollbar
        self.canvas = tk.Canvas(self, bg="white")  # Set background to white
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a frame inside the canvas
        self.text_frame = tk.Frame(self.canvas, bg="white")  # Set background to white
        self.canvas.create_window((0, 0), window=self.text_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configure scrolling
        self.text_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))


    def add_message(self, message, with_export=False):
        """Add a message to the chat display with an optional export button."""
        colour = "light grey" if "You:" in message else "grey"
        label = tk.Label(self.text_frame, text=message, anchor="w", justify="left", wraplength=350, bg=colour)
        label.pack(fill=tk.X, padx=10, pady=2, anchor="w")

        if with_export:
            export_button = tk.Button(self.text_frame, text="Export", command=lambda: self.export_message(message))
            export_button.pack(padx=10, pady=2, anchor="w")
            send_button = tk.Button(self.text_frame, text="Send to other chat mode", command=lambda: self.send_message_to_other_chat_mode(message, ChatMode.CODE_GENERATION))
            send_button.pack(padx=10, pady=2, anchor="w")

    def export_message(self, message):
        export_util.open_export_window(message)  # Open the export window to select file location
        logging.info("Message exported")
        
    def send_message_to_other_chat_mode(self, message, chat_mode):
        #*Send a message to another chat mode."""
        logging.info(f"Sending to chat mode: {chat_mode}")
        

def create_dropdown(parent, label_text, options, default_value):
    frame = tk.Frame(parent)
    frame.pack(padx=10, pady=5, anchor='w', fill=tk.X)

    label = tk.Label(frame, text=label_text)
    label.pack(side=tk.LEFT, padx=(0, 5), pady=5)

    selected_value = tk.StringVar(value=default_value)
    dropdown = ttk.Combobox(frame, textvariable=selected_value, values=options, state="readonly")
    dropdown.pack(side=tk.LEFT, pady=5)

    return selected_value

def create_chat_display(parent):
    chat_display = ScrollableTextWithButtons(parent)
    chat_display.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
    return chat_display

def send_message(chat_display, mode, selected_model, entry):
    user_message = entry.get().strip()
    if not user_message:
        chat_display.add_message("You: [Empty message]")
        return

    logging.info(f"Message received: {user_message}")
    chat_display.add_message(f"You: {user_message}")
    entry.delete(0, tk.END)

    # Use the selected model for response
    logging.info(f"Using chat model: {selected_model.get()}")
    response = chat_model.get_response(mode, selected_model.get(), user_message)
    chat_display.add_message(f"Bot: {response}", with_export=True)

def create_chat_tab(tab_control, mode):
    frame = ttk.Frame(tab_control)
    tab_control.add(frame, text=mode.value)

    # Get possible chat models based on the mode
    model_options = chat_model.get_possible_chat_models(mode)
    selected_model = create_dropdown(frame, "Select Model:", model_options, model_options[0])

    chat_display = create_chat_display(frame)
    # Add welcome message
    chat_display.add_message(f'Bot: {chat_model.get_welcome_message(mode)}')

    # Input frame with entry and send button
    input_frame = tk.Frame(frame)
    input_frame.pack(padx=10, pady=5, fill=tk.X)

    entry = tk.Entry(input_frame, width=40)
    entry.pack(side=tk.LEFT, padx=(0, 5), pady=5)

    send_button = tk.Button(input_frame, text='Send', command=lambda: send_message(chat_display, mode, selected_model, entry))
    send_button.pack(side=tk.LEFT, pady=5)

    entry.bind('<Return>', lambda event: send_message(chat_display, mode, selected_model, entry))

    return chat_display, entry

def start_chat_interface():
    root = tk.Tk()
    root.title(WINDOW_TITLE)
    root.geometry(WINDOW_SIZE)

    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=1, fill='both')

    # Create tabs for each chat mode
    chat_modes = ChatMode.__members__.values()
    for mode in ChatMode:
        create_chat_tab(tab_control, mode)

    root.mainloop()