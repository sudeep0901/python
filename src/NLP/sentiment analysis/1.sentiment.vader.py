#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'src\\NLP\sentiment analysis'))
	print(os.getcwd())
except:
	pass

import nltk

#%%
nltk.download()

#%%
from nltk.sentiment import vader
sia =  vader.SentimentIntensityAnalyzer()
#%%

sia.polarity_scores("What a terrible restaurent")
#%%
sia.polarity_scores("terrible")

#%%
sia.polarity_scores("Sudeep")


#%%
sia.polarity_scores(":)")


#%%
#polarity
sia.polarity_scores("the cumin was the kiss of death")

#%%
#punctuation
sia.polarity_scores("the food was good")

#%%
sia.polarity_scores("the food was good!")

#%%
# Negation
sia.polarity_scores("I am not well")

#%%
sia.polarity_scores("food not well")


#%%
sia.polarity_scores("food was not worst at all")

#%%
#Emphasis
sia.polarity_scores("food was GOOD")

#%%

from spellchecker import SpellChecker
spell = SpellChecker()
spell.correction("terrbile")
sent = []
#%%
for word in "food was terrbile and nto good at all".split(" "):
    sent.append(spell.correction(word))

sent = " ".join(sent)

#%%
sia.polarity_scores(sent)

#%%
#booster word
sia.polarity_scores("the food was so good, increases compound score")

#%%
# constrast
sia.polarity_scores("I usually hate seafood but I liked this")

#%%
# wrongly interpreted
sia.polarity_scores("I usually hate seafood and I liked this")

#%%
