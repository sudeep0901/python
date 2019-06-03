import nltk
sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""

tokens = nltk.word_tokenize(sentence)

print(tokens, type(tokens))
tags = nltk.pos_tag(tokens)
entities = nltk.chunk.ne_chunk(tags)
print(entities)
sentence = "sudeep patel"

tokens = nltk.word_tokenize(sentence)

print(tokens, type(tokens))

tags = nltk.pos_tag(tokens)
entities = nltk.chunk.ne_chunk(tags)
print(entities)
print(tags, type(tags))
# Identify named entities:

# Display a parse tree:

from nltk.corpus import treebank

t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()

