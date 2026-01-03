import re

class RuleBasedChatbot:
    def __init__(self):
        self.rules = {
            r'hi|hello|hey': "Hello! How can I assist you today?",
            r'how are you': "I'm just a computer program, but thanks for asking!",
            r'what is your name': "I am a chatbot.",
            r'weather': "I can't provide real-time weather updates, but I hope it's nice outside!",
            r'bye|goodbye': "Goodbye! Have a great day!",
            r'help': "You can ask me about the weather, my name, or just say hi!",
        }

    def respond(self, user_input):
        for pattern, response in self.rules.items():
            if re.search(pattern, user_input, re.IGNORECASE):
                return response
        return "I'm sorry, I don't understand that."

def main():
    chatbot = RuleBasedChatbot()

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()