# import neighboring file requirements_integration.py

import chat.requirements_integration as requirements_integration
import chat.code_generation as code_integration
import logging

from enum import Enum

# class syntax
class ChatMode(Enum):
    REQUIREMENTS = "Requirements Engineering"
    CODE_GENERATION = "Code Generation"
    
def get_possible_chat_models(mode):
    logging.info(f"Getting possible chat models for mode: {mode}")
    match mode:
        case ChatMode.REQUIREMENTS:
            return requirements_integration.get_possible_chat_models()
        case ChatMode.CODE_GENERATION:
            return code_integration.get_possible_chat_models()
        case _:
            logging.warning(f"Unknown mode: {mode}. Returning empty list.")
            # we should not reach here
            return []

def get_response(mode, selected_model, user_message):
    if not user_message.strip():
        return "Please enter a valid message."
    
    match mode:
        case ChatMode.REQUIREMENTS:
            logging.info(f"User story detected: {user_message}")     
            return requirements_integration.get_response(selected_model, user_message)
        case ChatMode.CODE_GENERATION:
            logging.info(f"Code snippet detected: {user_message}") 
            return code_integration.get_response(selected_model, user_message)
        case _:
            # Default response for other messages
            # we should not reach here
            logging.warning(f"Unknown mode: {mode}. Returning default response.")
            return "default"
        
    