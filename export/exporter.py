import logging

def export_message(file_path, message):    
    if file_path:
        if not file_path.endswith(".txt"):
            file_path = file_path + ".txt"  
        logging.info(f"File will be exported to: {file_path}")
        # Write the message to the selected file
        with open(file_path, "a") as file:
            file.write(message + "\n")
    else:
        logging.info("Export canceled.")