import tkinter as tk
from tkinter import filedialog
from export import exporter

def open_export_window(message):
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    try:
        # maybe other export variants at some point in time
        
        # Open a file dialog to select the export location
        file_path = filedialog.asksaveasfilename(
            title="Export File",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        exporter.export_message(file_path, message)
        
    finally:
        # Ensure the Tk instance is destroyed
        root.destroy()



