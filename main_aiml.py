import requests

API_KEY = "38e2363926214506bb913c1f2a89ab02"

def get_chatbot_response(prompt):
    url = 'https://api.aimlapi.com/chat/completions'
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }

    # Define the model and the prompt
    data = {
        'model': 'gpt-3.5-turbo',  # Use the appropriate model
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': 512,  
        'stream': False
    }

    # Make the POST request to OpenAI
    response = requests.post(url, headers=headers, json=data)

    # Check for errors
    if response.status_code == 200:
        response_json = response.json()
        # Extract the chatbot's message
        bot_message = response_json['choices'][0]['message']['content']
        return bot_message
    else:
        return "Error: " + response.text

# Main function to interact with the chatbot
def main():
    print("Chatbot is ready to talk! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        bot_response = get_chatbot_response(user_input)
        print("Chatbot:", bot_response)

if __name__ == '__main__':
    main()