import nltk
from nltk.sentiment import vader



sia = vader.SentimentIntensityAnalyzer()
sia.polarity_scores("How terrible")


sia.polarity_scores("terrible")
sia.polarity_scores(":D")
sia.polarity_scores(":-/")
sia.polarity_scores("the cumin was the kiss of death")
sia.polarity_scores("the food was good")
sia.polarity_scores("the food was good!")
sia.polarity_scores("the food was good!!")
sia.polarity_scores("the food was not good!!")
sia.polarity_scores("the food was not the worst!!")


sia.polarity_scores("the food was good")
sia.polarity_scores("the food was GOOD")
sia.polarity_scores("the food was so good")

sia.polarity_scores("I usually hate seafood but I liked this")
sia.polarity_scores("I usually hate seafood and I liked this")



from nltk.corpus import sentiwordnet as swn
swn.senti_synsets('dog')
swn.senti_synsets('dog')[3]




import nltk
from nltk.sentiment import vader

sia = vader.SentimentIntensityAnalyzer()
def vaderSentiment(review):
  return sia.polarity_scores(review)['compound']

review = "this is the best restaurant in the city"
vaderSentiment(review)

negatedReview = "this is not the best restaurant in the city"
vaderSentiment(negatedReview)

negatedReview = "this is not the worst restaurant in the city"
vaderSentiment(negatedReview)


positiveReviewsFileName = "/Users/vitthalsrinivasan/rt-polaritydata/rt-polaritydata/rt-polarity.pos"
negativeReviewsFileName = "/Users/vitthalsrinivasan/rt-polaritydata/rt-polaritydata/rt-polarity.neg"

with open(positiveReviewsFileName,'r') as f:
    positiveReviews = f.readlines()

with open(negativeReviewsFileName,'r') as f:
    negativeReviews = f.readlines()


def getReviewSentiments(sentimentCalculator): 
  negReviewResult = [sentimentCalculator(oneNegativeReview) for oneNegativeReview in negativeReviews]
  posReviewResult = [sentimentCalculator(onePositiveReview) for onePositiveReview in positiveReviews]
  return {'results-on-positive':posReviewResult, 'results-on-negative':negReviewResult}

def runDiagnostics(reviewResult):
  positiveReviewsResult = reviewResult['results-on-positive']
  negativeReviewsResult = reviewResult['results-on-negative']
  pctTruePositive = float(sum(x > 0 for x in positiveReviewsResult))/len(positiveReviewsResult)
  pctTrueNegative = float(sum(x < 0 for x in negativeReviewsResult))/len(negativeReviewsResult)
  totalAccurate = float(sum(x > 0 for x in positiveReviewsResult)) + float(sum(x < 0 for x in negativeReviewsResult))
  total = len(positiveReviewsResult) + len(negativeReviewsResult)
  print "Accuracy on positive reviews = " +"%.2f" % (pctTruePositive*100) + "%"
  print "Accurance on negative reviews = " +"%.2f" % (pctTrueNegative*100) + "%"
  print "Overall accuracy = " + "%.2f" % (totalAccurate*100/total) + "%"

runDiagnostics(getReviewSentiments(vaderSentiment))
















from nltk import word_tokenize
from nltk.corpus import sentiwordnet as swn


def superNaiveSentiment(review):
 reviewPolarity = 0.0
 numExceptions = 0
 for word in review.lower().split():
   weight = 0.0
   try:
     common_meaning = swn.senti_synsets(word)[0]
     if common_meaning.pos_score()>common_meaning.neg_score():
        weight = weight + common_meaning.pos_score()
     elif common_meaning.pos_score()<common_meaning.neg_score():
        weight = weight - common_meaning.neg_score()
   except:
       numExceptions = numExceptions + 1
   #print "Word: " + word + " weight: " + str(weight)
   reviewPolarity = reviewPolarity + weight
 return reviewPolarity



review = "this is the best restaurant in the city"
superNaiveSentiment(review)

negatedReview = "this is not the best restaurant in the city"
superNaiveSentiment(negatedReview)

negatedReview = "this is not the worst restaurant in the city"
superNaiveSentiment(negatedReview)


runDiagnostics(getReviewSentiments(superNaiveSentiment))





from string import punctuation 
from nltk.corpus import stopwords 
#from nltk.tokenize import word_tokenize



stopwords=set(stopwords.words('english')+list(punctuation))
def naiveSentiment(review):
 reviewPolarity = 0.0
 numExceptions = 0
 for word in review.lower().split():
   numMeanings = 0
   if word in stopwords:
     continue
   weight = 0.0
   try:
     for meaning in swn.senti_synsets(word):
       if meaning.pos_score() > meaning.neg_score():
          weight = weight + (meaning.pos_score() - meaning.neg_score())
          numMeanings = numMeanings + 1
       elif meaning.pos_score() < meaning.neg_score():
          weight = weight - (meaning.neg_score() - meaning.pos_score())
          numMeanings = numMeanings + 1
   except: 
       numExceptions = numExceptions + 1
   if numMeanings > 0:
     reviewPolarity = reviewPolarity + (weight/numMeanings)
 return reviewPolarity

review = "this is the best restaurant in the city"
naiveSentiment(review)

negatedReview = "this is not the best restaurant in the city"
naiveSentiment(negatedReview)

negatedReview = "this is not the worst restaurant in the city"
naiveSentiment(negatedReview)


runDiagnostics(getReviewSentiments(naiveSentiment))
