# import neighboring file requirements_integration.py

import chat.requirements_integration as requirements_integration
import logging

def decide_which_model(user_message):
    # Decide which model to use based on the user message
    logging.info(f"Deciding model for message: {user_message}")
    return requirements_integration.get_which_model(user_message)

def get_response(user_message):
    if not user_message.strip():
        return "Please enter a valid message."
    
    msg = decide_which_model(user_message)
    
    # decide if the user expects a user story or software code as answer
    if msg.lower().startswith("requirements"):
        logging.info(f"User story detected: {user_message}")
        # Here you can integrate with your actual chat model or logic        
        return f"User Story: {user_message}"
    elif msg.lower().startswith("code"):
        logging.info(f"Code snippet detected: {user_message}")
        return f"Code Snippet: {user_message}"
    else:
        # Default response for other messages
        # Here you can integrate with your actual chat model or logic   
        return "default"
    return f"Model decided: {msg}"


    