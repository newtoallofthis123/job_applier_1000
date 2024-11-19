# Module that connects to Ollama and sends and recieves data

import ollama

MODEL = "gemma2:2b"


def get_ollama_response(prompt):
    return ollama.generate(model=MODEL, prompt=prompt, stream=True)
