from .get_preconfigured_nlp import nlp


def lemmatize(text):
    return " ".join([token.lemma_ for token in nlp(text)])
