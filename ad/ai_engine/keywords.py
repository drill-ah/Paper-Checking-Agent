
import spacy

# Load spaCy model once
try:
    nlp = spacy.load("en_core_web_sm")
except:
    raise Exception("spaCy model not found. Run: python -m spacy download en_core_web_sm")


def extract_keywords(answer: str):
    """
    Extract NOUN, VERB, PROPER NOUN keywords
    Removes stopwords and duplicates
    """
    doc = nlp(answer)
    keywords = [
        token.lemma_.lower()
        for token in doc
        if token.pos_ in {"NOUN", "VERB", "PROPN"}
        and not token.is_stop
        and token.is_alpha
    ]
    return list(set(keywords))