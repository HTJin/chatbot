from fuzzywuzzy import fuzz
from ttsp import TextToSpeechPrinter
from stti import SpeechToTextInputer
import re


class ChatBot:
    def __init__(self):
        self.name = "BotFather"

    def save_user_name(self, user_name):
        self.user_name = user_name

    def get_user_intro(self):
        print("What is your name?")
        name = input("User: ")
        self.save_user_name(name)
        print(f"Welcome {self.user_name}")

    def get_response(self, user_input):
        fuzzy_match_threshold = 70  # adjust this as needed
        predefined_inputs = {
            "Hello": "Hi there!" if not self.user_name else f"Hi, {self.user_name}.",
            "How are you?": "I'm awesome, thanks for asking.",
            "Who are you?": f"I'm a chatbot, You can call me {self.name}.",
            "How do you convince people?": "I'm gonna make them an offer than can't refuse.",
            "What is your favorite food?": "Oranges and olive oil.",
            "What is the answer to life universe and everything": "42"
        }
        user_input_tokens = re.findall(r'\w+', user_input.lower())
        best_match = None
        best_match_ratio = 0

        for input_phrase in predefined_inputs:
            input_phrase_tokens = re.findall(r'\w+', input_phrase.lower())
            match_ratio = fuzz.partial_ratio(
                user_input_tokens, input_phrase_tokens)
            if match_ratio > best_match_ratio:
                best_match = input_phrase
                best_match_ratio = match_ratio

        if best_match and best_match_ratio >= fuzzy_match_threshold:
            return predefined_inputs[best_match]
        else:
            return "I'm sorry, I didn't understand that"

    def start_chat(self):
        print(f"Welcome! I'm {self.name}")
        self.get_user_intro()
        print("How can I assist you today?")
        while True:
            user_input = input("")
            if user_input.lower() == "quit":
                print("Bye! Have a great day!")
                break
            bot_response = self.get_response(user_input)
            print(bot_response)


if __name__ == "__main__":
    with TextToSpeechPrinter(), SpeechToTextInputer():
        ChatBot().start_chat()
