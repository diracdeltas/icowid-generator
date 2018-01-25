def join_words(words):
    return " ".join(word.split("::")[0] for word in words)
