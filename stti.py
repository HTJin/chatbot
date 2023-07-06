import speech_recognition as sr
import builtins
from beepy import beep


def play_sound():
    beep(sound="coin")


class SpeechToTextInputer:
    def __init__(self):
        self.r = sr.Recognizer()

    def read_line(self, *args):
        while True:
            with sr.Microphone() as source:
                play_sound()
                audio = self.r.record(source, 5)
            try:
                text = self.r.recognize_google(audio)
                if text:
                    return text
            except sr.UnknownValueError:
                print("Speech recognition could not understand audio")
            except sr.RequestError as e:
                print(
                    "Could not request results from Google Speech Recognition service; {0}".format(e))
            except Exception as e:
                print("I'm sorry there was an unknown error, please try again.")

    def __enter__(self):
        self.original_input = builtins.input
        builtins.input = self.read_line

    def __exit__(self, exc_type, exc_value, exc_traceback):
        builtins.input = self.original_input
