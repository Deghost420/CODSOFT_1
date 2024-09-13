
def simple_chatbot():
    print("Hello! I'm an enhanced chatbot. Ask me anything or type 'exit' to stop.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Bot: Goodbye!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hi there! How can I help you?")
        elif "how are you" in user_input:
            print("Bot: I'm doing well, thanks! How about you?")
        elif "your name" in user_input:
            print("Bot: I’m your friendly chatbot. You can call me Bot.")
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Bot: The current time is {current_time}.")
        elif "weather" in user_input:
            print("Bot: I can’t check the weather right now, but you can use a weather app.")
        elif "tell me a joke" in user_input:
            print("Bot: Why don't scientists trust atoms? Because they make up everything!")
        elif "bye" in user_input:
            print("Bot: Bye! Take care!")
            break
        elif "thank you" in user_input or "thanks" in user_input:
            print("Bot: You’re welcome! Happy to help.")
        elif "favorite color" in user_input:
            print("Bot: I don’t have a favorite color, but I think blue is cool!")
        elif "what can you do" in user_input:
            print("Bot: I can chat with you, tell jokes, and answer simple questions!")
        else:
            print("Bot: Hmm, I'm not sure how to respond to that. Could you try asking something else?")
            
simple_chatbot()
