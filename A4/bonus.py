import spacy

# Load the Dutch language model
nlp = spacy.load("nl_core_news_sm")

# Parse a sentence
sentence = "Mensen profiteren van een afgescheiden verhuizing die invloed heeft op drie amerikaanse autofabrieken en één in Quebec."
doc = nlp(sentence)

# Iterate over the parsed tokens
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)

