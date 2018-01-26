# icowid

generates random tweets based on erowid and ICO whitepapers (with some help
from r/ethtrader)

## instructions

### setup

* pip install [markovify](https://github.com/jsvine/markovify)

Run the following two commands at setup time and every time the corpus files
are updated:

* `make corpus`
* `make models`

### running

Run `make tweets`
