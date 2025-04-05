# import neighboring file requirements_integration.py

import chat.requirements_integration as requirements_integration
import chat.code_generation as code_integration
import logging


from enum import Enum

# class syntax
class ChatMode(Enum):
    REQUIREMENTS = "Requirements Engineering"
    CODE_GENERATION = "Code Generation"

def decide_which_model(user_message):
    # Decide which model to use based on the user message
    logging.info(f"Deciding model for message: {user_message}")
    return requirements_integration.get_which_model(user_message)

def get_response(mode, user_message):
    if not user_message.strip():
        return "Please enter a valid message."
    
    match mode:
        case ChatMode.REQUIREMENTS:
            logging.info(f"User story detected: {user_message}")
            # Here you can integrate with your actual chat model or logic        
            return requirements_integration.get_response(user_message)
        case ChatMode.CODE_GENERATION:
            logging.info(f"Code snippet detected: {user_message}") 
            return code_integration.get_response(user_message)
        case _:
            # Default response for other messages
            # Here you can integrate with your actual chat model or logic   
            return "default"
        
    