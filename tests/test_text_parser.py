from unittest import TestCase
from parsers.text_parser import TextParser

class TestTextParser(TestCase):
    
    def setUp(self):
        self.parser = TextParser()
    
    def test_get_words(self):
        text = "my test sentence"
        words = self.parser.get_words(text)
        self.assertEqual(len(words), 3)