print("🤖 RULE-BASED AI CHATBOT")
print("Bot: Hello! I am your AI Chatbot. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")
    user_input = user_input.lower().strip()   # handles caps/spaces

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! Nice to meet you.")
    elif user_input == "how are you":
        print("Bot: I am doing great! Thanks for asking.")
    elif user_input == "what is your name":
        print("Bot: I am the DecodeLabs Rule-Based Bot.")
    elif user_input in ["bye", "exit"]:
        print("Bot: Goodbye! Have a great day!")
        break
    else:
        print("Bot: I don't understand that yet.")
