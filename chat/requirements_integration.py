import ollama
import logging

model_id = "llama3.1:8b"
blind_response = "Hello I am a requirements integration model. I can help you with requirements and user stories."

def get_response(user_message):
    # Here you can integrate with your actual chat model or logic
    prompt = "You are a helpful assistant. Please generate a user story based on the following requirements: "
    prompt += f"User message: {user_message}"
    
    logging.info(f"Running Ollama ...")
    # answer = ollama.generate(model=model_id, prompt=prompt)
    answer = blind_response
    logging.info(f"Answer: {answer}")
    return answer.strip()