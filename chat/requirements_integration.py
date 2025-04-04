import ollama
import logging

model_id = "llama3.1:8b"
message = "Hello! What is the capital of France?"

def get_which_model(user_message):
    # Decide which model to use based on the user message
    prompt = "You are a helpful assistant. Please decide if the user wants to create user stories or code snippets. "
    prompt += "Depending on the results only answer in only one word: 'requirements' or 'code'. If it's not clear, answer 'default'. "
    logging.info(f"Using prompt: {prompt}")
    prompt += f"User message: {user_message}"
    
    logging.info(f"Running Ollama ...")
    answer = ollama.generate(model=model_id, prompt=prompt)
    logging.info(f"Answer: {answer['response']}")
    print(answer["response"])
    return answer["response"].strip()