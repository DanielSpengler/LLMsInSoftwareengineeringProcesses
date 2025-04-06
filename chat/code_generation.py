import ollama
import logging

model_id = "codellama:latest"
blind_response = "Hello I am a code generation model. I can help you with code snippets and programming tasks."

def get_response(selected_model, user_message):
    # Here you can integrate with your actual chat model or logic
    prompt = "You are a helpful assistant. Please generate a user story based on the following requirements: "
    prompt += f"User message: {user_message}"
    
    logging.info(f"Running Ollama ...")
    logging.info(f"Using model: {selected_model}")
    # answer = ollama.generate(model=model_id, prompt=prompt)
    answer = blind_response
    logging.info(f"Answer: {answer}")
    return answer.strip()