import requests
import time
from playsound import playsound
import os

API_KEY = "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"

def make_result_folder():
    current_directory = os.getcwd()
    subfolder_path = os.path.join(current_directory, 'results')
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)

def get_chatbot_response(prompt):
    url = 'https://api.openai.com/v1/audio/speech'
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }

    # Define the model and the prompt
    data = {
        'model': 'tts-1',  # Use the appropriate model
        'input': prompt,
        'voice': 'alloy',  # Controls randomness: lower is more focused and deterministic
    }

    # Make the POST request to OpenAI
    response = requests.post(url, headers=headers, json=data)

    # Check for errors
    if response.status_code == 200:
        timestamp = time.time()
        file_name = f'Response to {prompt} {timestamp}.mp3'
        file_path = f'results/{file_name}'
        with open(file_name, "wb") as f:
            f.write(response.content)
        playsound(file_name)
        return f'Audio file saved as {file_name}'
    else:
        return "Error: " + response.text

# Main function to interact with the chatbot
def main():
    print("Chatbot is ready to talk! Type 'exit' to quit.")
    make_result_folder()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        bot_response = get_chatbot_response(user_input)
        print("Chatbot:", bot_response)

if __name__ == '__main__':
    main()