def get_bot_response(user_input):
    """Determines the chatbot's reply based on predefined rules."""
    # Standardize input for easier matching
    text = user_input.strip().lower()
    
    # Rule-based logic using if-elif
    if text in ["hello", "hi", "hey"]:
        return "Hi!"
    elif "how are you" in text:
        return "I'm fine, thanks!"
    elif text in ["bye", "goodbye", "exit"]:
        return "Goodbye!"
    else:
        return "I'm a simple bot. Try saying 'hello', 'how are you', or 'bye'."

def start_chat():
    """Runs the main chat loop."""
    print("Chatbot started! Type 'bye' to exit.")
    
    # Continuous conversation loop
    while True:
        # Get input from the user
        user_input = input("\nYou: ")
        
        # Get and print the bot's response
        response = get_bot_response(user_input)
        print(f"Bot: {response}")
        
        # Break the loop if the user wants to leave
        if response == "Goodbye!":
            break

if __name__ == "__main__":
    start_chat()