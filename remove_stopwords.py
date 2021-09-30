import stop_words
import nlp


def remove_stopwords(text):
    doc = nlp(text)
    text = [X.text for X in doc]
    text_copy = text.copy()
    stopwords = stop_words.get_stop_words()
    for word in text:
        if word in stopwords:
            text_copy.remove(word)
    return " ".join(text_copy)
