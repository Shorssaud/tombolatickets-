from .configs.abbreviations import abbreviations



def transform_abbreviations(text):
    split_text = text.split(" ")
    for i in range(len(split_text)):
        for abbreviation in abbreviations:
            if split_text[i] == abbreviation[0]:
                split_text[i] = abbreviation[1]
    new_text = ""
    for word in split_text:
        if word:
            if new_text:
                new_text += " "
            new_text += word
    return new_text
