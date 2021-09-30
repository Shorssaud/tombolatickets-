from clean import clean, remove_useless_spaces
import string
from remove_stopwords import remove_stopwords
from lemmatize import lemmatize


def prepare_sentence(text):
    text = text.lower()
    text = clean(text)
    # text = lemmatize(text)
    # text = remove_stopwords(text)
    text = remove_useless_spaces(text)
    return text
