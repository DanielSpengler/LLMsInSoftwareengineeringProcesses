import ollama
import logging

from enum import Enum
from chat.chat_model_base import ChatModelBase

WELCOME_MESSAGE = "Hello I am a requirements integration model. I can help you with requirements and user stories."
blind_response = "This is a blind response. The actual model response will be generated later."

PROMPT = "you are an expert product owner and renowned for your concise user stories. these stories always include a motivation, a short description of wanted features and acceptance criteria. always start a user story with <user story> and end it with </user story>."
MESSAGE_WRAPPER = "create one or more user stories using the following message: '<message>'"

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
        prompt = MESSAGE_WRAPPER.replace("<message>", user_message)
                
        logging.info(f"Running Ollama ...")
        # find model_id from selected_model
        model_id = [model.value["model_id"] for model in PossibleModels if model.value["name"] == selected_model][0]
        logging.info(f"Using model: {selected_model} with id: {model_id}")
        
        if not self.is_model_running(model_id):
            # if model is not running, start it with PROMPT
            logging.info(f"Model {model_id} not running. Starting it with prompt.")
            ollama.generate(model=model_id, prompt=PROMPT)
            
        # answer = ollama.generate(model=model_id, prompt=prompt)
        answer = blind_response
        # FIXME Remove this log after testing
        logging.info(f"Answer: {answer}")
        return answer.strip()