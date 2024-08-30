import os
import ref.get_chatbot_response as chatbot_response
import ref.audio_record as audio_record

current_folder = os.getcwd()

# Main function to interact with the chatbot
def main():
    print("Chatbot is ready to talk! Type 'exit' to quit.")
    while True:
        print("You: ", end='\r')
        record_path = audio_record.main(current_folder)
        user_input = chatbot_response.get_transcription_response(record_path)
        # user_input = input("You: ")
        if 'bye' in user_input.lower():
            chatbot_response.get_sound_response("Goodbye! Have a good day!", current_folder)
            break
        bot_response = chatbot_response.get_text_response(user_input)
        print("Chatbot:", bot_response)
        chatbot_response.get_sound_response(bot_response, current_folder)

if __name__ == '__main__':
    main()