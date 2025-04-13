from abc import ABC, abstractmethod
import ollama

class ChatModelBase(ABC):
    @abstractmethod
    def get_possible_chat_models(self):
        """Return a list of possible chat models."""
        pass

    @abstractmethod
    def get_welcome_message(self):
        """Return a welcome message for the chat mode."""
        pass

    @abstractmethod
    def get_response(self, selected_model, user_message):
        """Generate a response based on the selected model and user message."""
        pass
    
    def is_model_running(model_name):
        processes = ollama.ps()  # get the list of running processes
        for process in processes.models:
            print(f"Process: {process}")
            if process.name == model_name:
                return True
        return False
        