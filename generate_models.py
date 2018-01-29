import markovify

with open('corpi/ico.txt') as f:
    text = f.read()
ico_model = markovify.Text(text, state_size=3).to_json()
with open('ico.json', 'w') as f:
    f.write(ico_model)

with open('corpi/erowid.txt') as f:
    text = f.read()
erowid_model = markovify.Text(text, state_size=3).to_json()
with open('erowid.json', 'w') as f:
    f.write(erowid_model)
