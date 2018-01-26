import sys
import markovify

with open('ico.json') as f:
    text = f.read()
ico_model = markovify.Text.from_json(text)

with open('erowid.json') as f:
    text = f.read()
erowid_model = markovify.Text.from_json(text)

# Combine models
combo = markovify.combine([ico_model, erowid_model], [1, 1])

for i in range(int(sys.argv[1])):
     print(combo.make_sentence())
