import markovify
import sys

with open('corpi/ico.txt') as f:
    text = f.read()
ico_model = markovify.Text(text)

with open('corpi/erowid.txt') as f:
    text = f.read()
erowid_model = markovify.Text(text)

# Combine models
combo = markovify.combine([ico_model, erowid_model], [3, 1])

for i in range(int(sys.argv[1])):
     print(combo.make_short_sentence(280))
