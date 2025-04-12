import tkinter as tk
from tkinter import filedialog

def open_export_window(message):
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    try:
        # Open a file dialog to select the export location
        file_path = filedialog.asksaveasfilename(
            title="Export File",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if file_path:
            if not file_path.endswith(".txt"):
                file_path = file_path + ".txt"  
            print(f"File will be exported to: {file_path}")
            # Write the message to the selected file
            with open(file_path, "a") as file:
                file.write(message + "\n")
        else:
            print("Export canceled.")
    finally:
        # Ensure the Tk instance is destroyed
        root.destroy()



