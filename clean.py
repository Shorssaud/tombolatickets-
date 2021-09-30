import re
import emoji
import string
import regex
from .configs.replacements import replacements


def clean(t):
    t = replace_generics(t)
    t = replace_emojis(t)
    t = replace_punctuations(t)

    return t


def replace_generics(t):
    for step in replacements:
        t = re.sub(step[0], step[1], t)
    return t


def replace_emojis(t):
    data = regex.findall(r'\X', t)
    for word in data:
        if any(char in emoji.UNICODE_EMOJI['en'] for char in word):
            t = re.sub(word, '', t)
    return t


def replace_punctuations(t):
    punctuation = string.punctuation.replace("'", "")
    t = re.sub("[" + (punctuation[0:11] + punctuation[12:]) + "]", "", t)
    return re.sub(r'\s+', ' ', t).strip()


def remove_useless_spaces(t):
    new = ""
    for i in range (len(t)):
        if (t[i] == ' ' and t[i + 1] and t[i + 1] == ' '):
            continue
        new += t[i]
    return new