# icowid

generates markov chain sentences based on erowid trip reports and ICO
whitepapers.

used for https://twitter.com/icowid

## instructions

### setup

* install python3
* pip3 install [markovify](https://github.com/jsvine/markovify)

run the following two commands at setup time and every time the corpus files
are updated:

* `make corpus`
* `make models`

### running

run `make sentences`

this generates a batch of 20 sentences. edit `Makefile` to change the batch size.

## contributing ICO whitepapers

contributions to the corpus of ICO whitepapers are highly welcome!

1. if in PDF format, convert the paper to a .txt file (ex: using pdftotext or the Automator tool on MacOS). make sure the output text file doesn't look too f'ed up.
2. put the text file in `corpi/ico_text/`
3. open a pull request
