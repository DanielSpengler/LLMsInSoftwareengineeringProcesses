from chat.requirements_integration import RequirementsIntegration
from chat.code_generation import CodeGeneration
from enum import Enum
import logging

# Enum for chat modes
class ChatMode(Enum):
    REQUIREMENTS = "Requirements Engineering"
    CODE_GENERATION = "Code Generation"

# Map modes to their respective implementations
chat_mode_mapping = {
    ChatMode.REQUIREMENTS: RequirementsIntegration(),
    ChatMode.CODE_GENERATION: CodeGeneration(),
}

def get_possible_chat_models(mode):
    logging.info(f"Getting possible chat models for mode: {mode}")
    chat_model = chat_mode_mapping.get(mode)
    if chat_model:
        return chat_model.get_possible_chat_models()
    logging.warning(f"Unknown mode: {mode}. Returning empty list.")
    return []

def get_welcome_message(mode):
    logging.info(f"Getting welcome message for mode: {mode}")
    chat_model = chat_mode_mapping.get(mode)
    if chat_model:
        return chat_model.get_welcome_message()
    logging.warning(f"Unknown mode: {mode}. Returning empty string.")
    return ""

def get_response(mode, selected_model, user_message):
    if not user_message.strip():
        return "Please enter a valid message."
    
    chat_model = chat_mode_mapping.get(mode)
    if chat_model:
        return chat_model.get_response(selected_model, user_message)
    
    logging.warning(f"Unknown mode: {mode}. Returning default response.")
    return "default"

