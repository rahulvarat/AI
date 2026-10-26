
def chatbot():
    print("Chatbot: Hello! Welcome to the chatbot.")
    print("Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if "hello" in user or "hi" in user:
            print("Chatbot: Hello! How can I help you?")

        elif "your name" in user:
            print("Chatbot: I am a simple rule-based chatbot.")

        elif "how are you" in user:
            print("Chatbot: I am fine. Thank you!")

        elif "your purpose" in user:
            print("Chatbot: I answer questions using predefined rules.")

        elif "thank" in user:
            print("Chatbot: You are welcome!")

        elif "bye" in user:
            print("Chatbot: Goodbye! Have a nice day.")
            break

        else:
            print("Chatbot: Sorry, I don't understand.")


chatbot()
