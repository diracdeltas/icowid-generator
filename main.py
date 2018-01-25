import markovify

with open('corpi/ico.txt') as f:
    text = f.read()
ico_model = markovify.Text(text)

with open('corpi/erowid.txt') as f:
    text = f.read()
erowid_model = markovify.Text(text)

# Combine models
combo = markovify.combine([ico_model, erowid_model], [2, 1])

for i in range(50):
     print(combo.make_short_sentence(280))
