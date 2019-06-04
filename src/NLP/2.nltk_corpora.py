import nltk
import os

# nltk.download()
print(os.listdir(nltk.data.find("corpora")))

from nltk.corpus import brown
brown.words()

nltk.corpus.gutenberg.fileids()
hemlet= nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
print(hemlet, type(hemlet))

for word in hemlet[:500]:
    print(word, sep=" ", end = " ")


AI = """The modern definition of artificial intelligence (or AI) is "the study and design of intelligent agents" where an intelligent agent is a system that perceives its environment and takes actions which maximizes its chances of success.

John McCarthy, who coined the term in 1956, defines it as "the science and engineering of making intelligent machines."

Other names for the field have been proposed, such as computational intelligence, synthetic intelligence or computational rationality.

The term artificial intelligence is also used to describe a property of machines or programs: the intelligence that the system demonstrates.

AI research uses tools and insights from many fields, including computer science, psychology, philosophy, neuroscience, cognitive science, linguistics, operations research, economics, control theory, probability, optimization and logic.

AI research also overlaps with tasks such as robotics, control systems, scheduling, data mining, logistics, speech recognition, facial recognition and many others.

Computational intelligence Computational intelligence involves iterative development or learning (e.g., parameter tuning in connectionist systems).

Learning is based on empirical data and is associated with non-symbolic AI, scruffy AI and soft computing.

Subjects in computational intelligence as defined by IEEE Computational Intelligence Society mainly include: Neural networks: trainable systems with very strong pattern recognition capabilities.

Fuzzy systems: techniques for reasoning under uncertainty, have been widely used in modern industrial and consumer product control systems; capable of working with concepts such as 'hot', 'cold', 'warm' and 'boiling'.

Evolutionary computation: applies biologically inspired concepts such as populations, mutation and survival of the fittest to generate increasingly better solutions to the problem.

These methods most notably divide into evolutionary algorithms (e.g., genetic algorithms) and swarm intelligence (e.g., ant algorithms).

With hybrid intelligent systems, attempts are made to combine these two groups.

Expert inference rules can be generated through neural network or production rules from statistical learning such as in ACT-R or CLARION.

It is thought that the human brain uses multiple techniques to both formulate and cross-check results.
Thus, systems integration is seen as promising and perhaps necessary for true AI, especially the integration of symbolic and connectionist models."""

from nltk import word_tokenize

AI_Toknes =  word_tokenize(AI)
print(AI_Toknes)
print(len(AI_Toknes))

from nltk.probability import FreqDist
fdist = FreqDist()  

for word in AI_Toknes:
    fdist[word.lower()] +=1

print(fdist.elements)

print(fdist['artificial'], len(fdist))

# top10
fdist_top10 = fdist.most_common(10)
print(fdist_top10)

from nltk.tokenize import blankline_tokenize

# para separated by new line
AI_blank = blankline_tokenize(AI)
len(AI_blank)
print(AI_blank[2])

# bigrams

from nltk.util import bigrams, trigrams, ngrams

qt ="""The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.
Read more at: https://www.brainyquote.com/quotes/helen_keller_101301"""

quotes_token = nltk.word_tokenize(qt)

quotes_bigrams = list(nltk.bigrams(quotes_token))
print(quotes_bigrams)

quotes_trigrams = list(nltk.trigrams(quotes_token))
print(quotes_trigrams)

quotes_quadgrams = list(nltk.ngrams(quotes_token, 4 ))
print(quotes_quadgrams)

# stemming
from nltk import PorterStemmer

pst = PorterStemmer()
pst.stem("having")
pst.stem("sudeep")

words_stem = ["give", "giving", "given", "gave"]
for words in words_stem:
    print(words + " :" + pst.stem(words))

from nltk import LancasterStemmer

lnst = LancasterStemmer()
for words in words_stem:
    print(words + " :" + lnst.stem(words))

from nltk import SnowballStemmer

snl = SnowballStemmer("english")
for words in words_stem:
    print(words + " :" + snl.stem(words))

# lemmetizing

from nltk import WordNetLemmatizer
wordnet = WordNetLemmatizer()

for words in words_stem:
    print(words + " :" + wordnet.lemmatize(words))

# pos parts of speech


# stopwords
from nltk.corpus import stopwords

stopwords.words("english")
print(len(stopwords.words("english")))

import re
punctuation = re.compile(r'[-.?,:;()|{}|0-9]')
post_punctuation = []

for words in AI_Toknes:
    word = punctuation.sub("", words)
    if len(word) > 0:
        post_punctuation.append(word)

print(post_punctuation)


#parts of speech Tags & Descriptoin

tag_string = "I am really loving it and it is facinating"
tag_tokens = word_tokenize(tag_string)

for token in tag_tokens:
    print(nltk.pos_tag([token]))


# NER - Names Entity Recognition
from nltk import ne_chunk

NE_sent = "The Indian prime minister is Modi"
NE_tokenize = word_tokenize(NE_sent)

NE_tags = nltk.pos_tag(NE_tokenize)
print(NE_tags)

nltk.download('maxent_ne_chunker')

NE_ner = ne_chunk(NE_tags)
print(NE_ner)