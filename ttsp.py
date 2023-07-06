import pyttsx3
import sys


class TextToSpeechPrinter:
    def __init__(self):
        self.engine = pyttsx3.init()

    def __enter__(self):
        self.original_print = print

        def tts_print(*args, **kwargs):
            text = " ".join(str(arg) for arg in args)
            self.engine.say(text)
            self.engine.runAndWait()

        sys.stdout.write = tts_print

    def __exit__(self, exc_type, exc_value, trace):
        sys.stdout.write = self.original_print
