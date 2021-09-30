import hashlib
from prepare_sentence import prepare_sentence


def describe_sentence(text):
    normalized = prepare_sentence(text)
    return {
        "raw": text,
        "normalized": normalized,
        "hash": hashlib.md5(normalized.encode()).hexdigest()
    }
