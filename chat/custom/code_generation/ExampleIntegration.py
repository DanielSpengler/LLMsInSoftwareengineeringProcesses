import logging

def get_response(self, selected_model, user_message):
    logging.info(f"Running custom integration for model: {selected_model} using message {user_message}")
    return "This is a custom response. The actual model response will be generated later."