import markovify
import re
import spacy
import util

nlp = spacy.load("en")

class BetterText(markovify.Text):
    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        return util.join_words(words)


with open('corpi/ico.txt') as f:
    text = f.read()
ico_model = BetterText(text, state_size=3).to_json()
with open('ico.json', 'w') as f:
    f.write(ico_model)

with open('corpi/erowid.txt') as f:
    text = f.read()
erowid_model = BetterText(text, state_size=3).to_json()
with open('erowid.json', 'w') as f:
    f.write(erowid_model)


