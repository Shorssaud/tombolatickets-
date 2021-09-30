from .clean import replace_punctuations, replace_generics, replace_emojis, remove_useless_spaces
from .string import remove_accents
from .remove_stopwords import remove_stopwords
from .lemmatize import lemmatize
from .transform_abbreviations import transform_abbreviations


def prepare_sentence(text):
    text = text.lower()
    text = replace_punctuations(text)
    text = transform_abbreviations(text)
    text = replace_generics(text)
    text = replace_emojis(text)
    text = lemmatize(text)
    text = remove_accents(text)
    text = remove_stopwords(text)
    text = remove_useless_spaces(text)
    return text
