# icowid

markov bot to make tweets based on trump tweets + erowid. thanks to
http://www.trumptwitterarchive.com/archive for the trump tweets.

## instructions

### setup

* pip install [markovify](https://github.com/jsvine/markovify)

Run the following two commands at setup time and every time the corpus files
are updated:

* `make corpus`
* `make models`

### running

Run `make tweets`
