import re

def chatbot_response(user_input):
    """Simple chatbot that responds based on predefined rules."""
    user_input = user_input.lower()  # Convert to lowercase for better matching

    # Greetings
    if re.search(r'\b(hi|hello|hey|hola|namaste)\b', user_input):
        return "Hello! How can I assist you today? 😊"
    
    # Asking about the chatbot
    elif re.search(r'\b(who are you|what can you do)\b', user_input):
        return "I'm a simple chatbot that can answer basic queries. Try asking me something!"

    # Asking about time or date
    elif re.search(r'\b(time|date|day)\b', user_input):
        from datetime import datetime
        return f"The current date and time is: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    # Weather-related questions
    elif re.search(r'\b(weather|temperature|forecast)\b', user_input):
        return "I can't fetch real-time weather updates yet, but you can check a weather website like weather.com! ☀️"

    # Goodbye messages
    elif re.search(r'\b(bye|goodbye|see you)\b', user_input):
        return "Goodbye! Have a great day! 👋"

    # Default response for unknown inputs
    else:
        return "I'm not sure how to respond to that. Can you ask me something else?"

# Main chatbot loop
if __name__ == "__main__":
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_message = input("You: ")
        if user_message.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! 👋")
            break
        response = chatbot_response(user_message)
        print("Chatbot:", response)