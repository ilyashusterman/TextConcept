import nltk

class TextParser:

    def __init__(self):
        nltk.download('punkt')

    @classmethod
    def get_words(cls, text):
        return nltk.word_tokenize(text)