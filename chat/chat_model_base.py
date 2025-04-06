from abc import ABC, abstractmethod

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