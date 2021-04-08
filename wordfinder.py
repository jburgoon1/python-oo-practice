"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
    
    def __init__(self, words):
        
        word = open('words.txt',"r")
        self.words = self.read(word)
        print(f'{len(self.words)} words read')
    def read(self, word):
        return [words.strip() for words in word 
        if words.strip() and not words.startswith("#")]
    def random(self):
        return random.choice(self.words)
wordFind = WordFinder('words.txt')
