import nltk
from nltk.book import *
from nltk.text import Text
print(text1)
text1.concordance("monstrous")
type(text1)
text11 = Text("Hellow sudeeep","mytext")
print(text11)
text11.similar("sud")
text11.concordance("sudeeep")
text1.similar("monster")
text2.common_contexts(["monstrous", 'very'])
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])