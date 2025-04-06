import ollama
import logging

from enum import Enum
from chat.chat_model_base import ChatModelBase

WELCOME_MESSAGE = "Hello I am a requirements integration model. I can help you with requirements and user stories."
blind_response = "This is a blind response. The actual model response will be generated later."

class PossibleModels(Enum):
    LLAMA3 = {"name": "Llama 3.1", "model_id": "llama3.1:8b"}
    MIXTRAL = {"name": "Mixtral", "model_id": "mixtral"}
    DEEPSEEKR1 = {"name": "DeepSeek R1", "model_id": "deepseek-r1:8b-llama-distill-q8_0"}

class RequirementsIntegration(ChatModelBase):
    def get_possible_chat_models(self):
        return [model.value["name"] for model in PossibleModels]

    def get_welcome_message(self):
        return WELCOME_MESSAGE

    def get_response(self, selected_model, user_message):
        prompt = "You are a helpful assistant. Please generate a user story based on the following requirements: "
        prompt += f"User message: {user_message}"
        
        logging.info(f"Running Ollama ...")
        # find model_id from selected_model
        model_id = [model.value["model_id"] for model in PossibleModels if model.value["name"] == selected_model][0]
        logging.info(f"Using model: {selected_model} with id: {model_id}")
        # answer = ollama.generate(model=model_id, prompt=prompt)
        answer = blind_response
        logging.info(f"Answer: {answer}")
        return answer.strip()