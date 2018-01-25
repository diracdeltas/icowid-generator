# icowid

generates random tweets based on erowid and ICO whitepapers

## instructions

* pip install [markovify](https://github.com/jsvine/markovify)
* only needed if generating text from PDFs: install https://textract.readthedocs.io/en/latest/installation.html
* spacy: https://spacy.io/
* `./corpi/combine_all.sh`
* `python main.py $NUMBER_OF_SENTENCES_TO_GENERATE > output.log`
