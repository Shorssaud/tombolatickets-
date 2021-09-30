from .get_stopwords import get_stopwords
from .get_preconfigured_nlp import nlp


def remove_stopwords(text):
    doc = nlp(text)
    text = [X.text for X in doc]
    text_copy = text.copy()
    stopwords = get_stopwords()
    for word in text:
        if word in stopwords:
            text_copy.remove(word)
    return " ".join(text_copy)
